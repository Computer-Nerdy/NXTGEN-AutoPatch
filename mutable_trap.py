# Chaos Lab: Mutable Default Argument Trap
def add_to_registry(user_id, registry=[]):
    """
    BUG: The 'registry' list is shared across all function calls.
    INTENT: Each call should start with a fresh list unless one is provided.
    """
    registry.append(user_id)
    return registry

if __name__ == "__main__":
    print(f"Call 1 (Expected ['A']): {add_to_registry('A')}")
    print(f"Call 2 (Expected ['B']): {add_to_registry('B')}") 
    # Current Output: ['A', 'B'] <- This is the bug!
