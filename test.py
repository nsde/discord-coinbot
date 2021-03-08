import time

tic = time.perf_counter()
# ===================================================================

import threading

globals()['i'] = 0

def zaehler_plus():
    for _ in range(10000000):
        globals()['i'] += 1

plus_thread = threading.Thread(target=zaehler_plus)
plus_thread.start()


for _ in range(10000000):
    globals()['i'] -= 1

print(globals()['i'])

# ===================================================================
toc = time.perf_counter()

print(f"Took {toc - tic:0.4f} seconds")