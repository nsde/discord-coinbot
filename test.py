import time

tic = time.perf_counter()
# ===================================================================

from deep_translator import GoogleTranslator
translated = GoogleTranslator(source='auto', target='de').translate("keep it up, you are awesome")  # output -> Weiter so, du bist großartig
print(translated)

# ===================================================================
toc = time.perf_counter()

print(f"Took {toc - tic:0.4f} seconds")