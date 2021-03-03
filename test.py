import time

tic = time.perf_counter()
# ===================================================================

from skingrabber import skingrabber

sg = skingrabber()

response = sg.get_skin_rendered(user='onlixx')
print(response)

# ===================================================================
toc = time.perf_counter()

print(f"Took {toc - tic:0.4f} seconds")