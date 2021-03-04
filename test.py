import time

tic = time.perf_counter()
# ===================================================================

print(['hallo', 'test', '123'][:-1])

# ===================================================================
toc = time.perf_counter()

print(f"Took {toc - tic:0.4f} seconds")