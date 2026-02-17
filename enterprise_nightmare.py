# Chaos Lab: Enterprise Nightmare Stress Test
import threading
import time

data_log = []
leak_storage = []

def process_transaction(amount):
    global data_log
    # BUG 1: Race Condition on global list
    data_log.append(amount)
    
    # BUG 2: Memory Leak (simulating a cache that never clears)
    leak_storage.append(bytearray(1024 * 500)) 
    
    # BUG 3: Logic/Math Error
    # Intent: 8% tax. Mistake: 0.08% tax for high values.
    if amount > 500:
        return amount + (amount * 0.08 / 100) 
    return amount * 1.08

# Run a quick test
print(f"Processing $1000: {process_transaction(1000)}")
