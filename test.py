import time

tic = time.perf_counter()
# ===================================================================

from youtubesearchpython import *
video = Video.get("https://youtu.be/6ONRf7h3Mdk")
print(video['description'][:100])

# ===================================================================
toc = time.perf_counter()

print(f"Took {toc - tic:0.4f} seconds")