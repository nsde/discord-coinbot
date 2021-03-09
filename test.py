import time

tic = time.perf_counter()
# ===================================================================

print(66666 % 111)

# ===================================================================
toc = time.perf_counter()

print(f"Took {toc - tic:0.4f} seconds")