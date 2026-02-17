import sys
import subprocess
import os
import time
import hashlib
import google.generativeai as genai
from rich.console import Console
from rich.panel import Panel
from rich.syntax import Syntax
from rich.table import Table


API_KEY = os.getenv("GEMINI_API_KEY")
if not API_KEY:
    raise RuntimeError("❌ GEMINI_API_KEY not set in environment")

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-3-flash-preview")

console = Console()
CACHE = {}


def hash_code(code: str) -> str:
    return hashlib.sha256(code.encode()).hexdigest()

def run_script(script_name):
    try:
        return subprocess.run(
            [sys.executable, script_name],
            capture_output=True,
            text=True,
            timeout=5,
            input="10\n"
        )
    except subprocess.TimeoutExpired:
        class FakeResult:
            returncode = 1
            stderr = "⏰ TIMEOUT ERROR: Possible infinite loop."
            stdout = ""
        return FakeResult()

def safe_generate(prompt):
    for attempt in range(3):
        try:
            return model.generate_content(prompt).text
        except Exception as e:
            if "429" in str(e):
                wait = 60 * (attempt + 1)
                console.print(f"[yellow]⏳ Rate limited. Waiting {wait}s...[/yellow]")
                time.sleep(wait)
            else:
                raise
    raise RuntimeError("❌ Gemini failed after retries")

def get_ai_response(prompt, code_hash):
    if code_hash in CACHE:
        return CACHE[code_hash]

    text = safe_generate(prompt)
    text = text.replace("```python", "").replace("```", "").strip()

    if text.strip() == "CLEAN":
        CACHE[code_hash] = "CLEAN"
        return "CLEAN"

    CACHE[code_hash] = text
    return text

def analyze_and_fix(target_file, result):
    with open(target_file, "r") as f:
        code = f.read()

    code_hash = hash_code(code)

    if result.returncode != 0:
        context = f"ERROR DETECTED:\n{result.stderr}"
        task_type = "CRASH FIX"
    else:
        context = f"OBSERVED OUTPUT:\n{result.stdout}"
        task_type = "LOGIC AUDIT"

    prompt = f"""
ACT AS A SENIOR FULL-STACK ENGINEER AND QA EXPERT.
Perform a {task_type} on the provided Python code.

[CONTEXT]
{context}

[SOURCE CODE]
{code}

[REQUIRED RESPONSE STRUCTURE]
You MUST follow this format exactly:

1. [REASONING]
   - Identify the intent of the code as COMMENT LINES.
   - List every bug found (syntax, runtime, or logical) as COMMENT LINES.
   - Explain the step-by-step fix strategy as COMMENT LINES.
   - Mention any edge cases handled (e.g., ZeroDivision, Empty Lists) as COMMENT LINES.

2. [FIXED_CODE]
   - Provide the complete, runnable Python code.
   - Use ONLY markdown formatting for DOCUMENTATION but NOT the code itself.
   - Ensure the code is ready for immediate execution.
   - Do NOT 
"""
    return get_ai_response(prompt, code_hash), task_type

def main():
    console.print(Panel.fit("⚡ AUTOPATCH: RESET & HEAL ⚡", border_style="cyan"))

    if len(sys.argv) < 2:
        console.print("[red]Usage: python AUTOPATCH_BACKEND.py <script.py>[/red]")
        return

    target = sys.argv[1]

    with open(target) as f:
        original_code = f.read()

    res1 = run_script(target)
    fix1, mode1 = analyze_and_fix(target, res1)

    if fix1 == "CLEAN":
        console.print(Panel("✨ Code is already correct!", border_style="green"))
        return

    with open(target, "w") as f:
        f.write(fix1)

    console.print(f"[yellow]⚠️ {mode1} applied. Verifying...[/yellow]")

    res2 = run_script(target)
    fix2, mode2 = analyze_and_fix(target, res2)

    if fix2 != "CLEAN":
        console.print(f"[red]🚨 Second issue detected ({mode2}). Applying final patch.[/red]")
        with open(target, "w") as f:
            f.write(fix2)

    with open(target) as f:
        final_code = f.read()

    table = Table(title="Final Self-Healed Patch")
    table.add_column("Original", style="dim")
    table.add_column("Final", style="green")

    table.add_row(
        Syntax(original_code, "python"),
        Syntax(final_code, "python")
    )

    console.print(table)

if __name__ == "__main__":

    main()
