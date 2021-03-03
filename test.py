import time

tic = time.perf_counter()
# ===================================================================

from gtts import gTTS
import os

tts = gTTS('Hallo ich bin Felix.', lang='de')
tts.save('file.mp3')
os.system('start file.mp3')

# ===================================================================
toc = time.perf_counter()

print(f"Took {toc - tic:0.4f} seconds")