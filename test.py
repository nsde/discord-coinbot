import time

tic = time.perf_counter()
# ===================================================================

mylist = ['dog', 'cat', 'dolphin', 'parrot']
for animal in mylist: print(animal)

# ===================================================================
toc = time.perf_counter()

print(f"Took {toc - tic:0.4f} seconds")