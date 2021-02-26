import time

tic = time.perf_counter()
# ===================================================================

import meme_get

a = meme_get.RedditMemes()
meme_list = a.get_memes(1)
print(meme_list[0]._pic_url)

# ===================================================================
toc = time.perf_counter()

print(f"Took {toc - tic:0.4f} seconds")