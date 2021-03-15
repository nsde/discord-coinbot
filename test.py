import time

tic = time.perf_counter()
# ===================================================================

print('Hello'[-2:])

# ===================================================================
toc = time.perf_counter()

print(f"Took {toc - tic:0.4f} seconds")