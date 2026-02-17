# ⚡ NXTGEN-AutoPatch

[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue)](https://www.python.org/)
[![AI Model](https://img.shields.io/badge/AI%20Model-Gemini%203%20Flash-orange)](https://deepmind.google/technologies/gemini/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

**NXTGEN-AutoPatch** is an autonomous, self-healing AI debugging agent designed to bridge the gap between "code that runs" and "code that works." By leveraging the **Gemini 3 Flash** engine, it performs deep semantic analysis to repair runtime crashes, logical flaws, and latent architectural risks in real-time.

> "Turns crappy code into production-grade assets instantly." 🚀💀

---

## 📖 Table of Contents
1. [Core Capabilities](#-core-capabilities)
2. [Technical Architecture](#-technical-architecture)
3. [The Self-Healing Loop](#-the-self-healing-loop)
4. [Installation & Setup](#-installation--setup)
5. [Usage & Examples](#-usage--examples)
6. [Advanced Logic Auditing](#-advanced-logic-auditing)

---

## 🧠 Core Capabilities

Unlike traditional linters, NXTGEN-AutoPatch operates on **Intent**. It understands the "Why" behind your "How."

* **⚡ Semantic Intent Analysis**: Corrects math logic (e.g., inverted transaction math) based on variable names and context.
* **🛡️ Thread Safety & Concurrency**: Identifies race conditions and automatically implements `threading.Lock()` and atomic operations.
* **🧹 Resource Management**: Detects memory leaks and suggests optimized data structures like `deque`.
* **🧪 Edge Case Hardening**: Proactively adds validation for ZeroDivision, TypeErrors, and empty data sets.
* **✨ Professional CLI**: Powered by `rich`, featuring side-by-side "Original vs. Healed" diffs and "Inner Monologue" reasoning traces.

---

## 🏗️ Technical Architecture

NXTGEN-AutoPatch is built on a "Ghost-in-the-Shell" execution model:

1.  **Isolated Execution**: Uses Python's `subprocess` to run target scripts in a sandbox with a 5-second timeout and automated dummy inputs ("10") to prevent hanging on infinite loops or `input()` calls.
2.  **Context Injection**: Combines the script's source code, error logs (stderr), and observed outputs (stdout) into a high-density prompt for the Gemini 3 Flash model.
3.  **Reflective Reasoning**: Uses a **Chain-of-Thought (CoT)** prompt structure, forcing the AI to document its "Inner Monologue" before outputting code.

---

## 🔄 The Self-Healing Loop

NXTGEN-AutoPatch employs a **Two-Round Verification System** to ensure 100% stable patches:

* **Round 1: Initial Repair**: The agent identifies the primary crash or logical flaw and applies a first-pass patch.
* **Round 2: Secondary Audit**: The agent re-executes the *patched* code and performs a "Self-Reflection" audit to check for side effects or missed logic.

---

## 🚀 Installation & Setup

### Prerequisites
* Python 3.10+
* A Google AI Studio API Key (Gemini 3 Flash)

### Setup
```bash
# Clone the repository
git clone [https://github.com/Computer-Nerdy/NXTGEN-AutoPatch.git](https://github.com/Computer-Nerdy/NXTGEN-AutoPatch.git)
cd NXTGEN-AutoPatch

# Install dependencies
pip install -r requirements.txt

# Set your API Key
export GEMINI_API_KEY="your_api_key_here"
$env:GEMINI_API_KEY="YOUR_API_KEY_FROM_GOOGLE"
python AUTOPATCH.py YOUR_FILE.py renamed as broken.py

```

## 🛠️ Usage & Examples

### Basic Usage
To fix a script, simply run the agent against your target file:
```bash
python autopatch.py my_script.py
```

The "Enterprise Nightmare" Stress Test
NXTGEN-AutoPatch is designed to handle complex, multi-threaded scripts. You can test its limits using our sample stress test:

python autopatch.py examples/enterprise_nightmare.py

This test includes:

Mutable Default Argument bugs: Identifies task_queue=[] traps that leak state across calls.

Global state race conditions: Detects unsynchronized access to shared resources across multiple threads.

Infinite memory leakage simulation: Spots ever-growing buffers and suggests optimized management.

Subtle logic errors: Corrects incorrect math in percentage calculations that don't trigger crashes.

## 🔍 Advanced Logic Auditing

NXTGEN-AutoPatch is specifically tuned to catch "Silent Killers"—bugs that produce incorrect results without triggering a crash:

* **Race Condition Detection**: Identifies unsynchronized access to shared global resources and implements necessary locking mechanisms.
* **Semantic Math Verification**: Compares variable names (e.g., `tax`, `balance`) with mathematical operations to identify and flip inverted logic.
* **Mutable Default Argument Audit**: Scans function signatures for initialized `list` or `dict` objects that cause unexpected state leakage between calls.
* **Resource Leak Analysis**: Recognizes data structures that grow monotonically without a clear termination or clearing path, preventing memory exhaustion.
