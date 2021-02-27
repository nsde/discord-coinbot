import time

tic = time.perf_counter()
# ===================================================================

import os; os.system("echo hello")

# ===================================================================
toc = time.perf_counter()

print(f"Took {toc - tic:0.4f} seconds")