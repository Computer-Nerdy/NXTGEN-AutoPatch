# Chaos Lab: The Threading Nightmare
import threading

balance = 0

def deposit():
    global balance
    for _ in range(100000):
        # BUG: No threading.Lock() used. 
        # Race condition occurs during the read-modify-write cycle.
        balance += 1

t1 = threading.Thread(target=deposit)
t2 = threading.Thread(target=deposit)

t1.start(); t2.start()
t1.join(); t2.join()

print(f"Final Balance: {balance}") 
# Expected: 200000 | Actual: Usually something like 143201
