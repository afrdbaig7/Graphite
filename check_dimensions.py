from PIL import Image
import os

files = ['test-export-1x.png', 'test-export-2x.png', 'test-export-8x.png']

for filename in files:
    if os.path.exists(filename):
        img = Image.open(filename)
        print(f"{filename}: {img.width}x{img.height}")
        img.close()
    else:
        print(f"{filename}: NOT FOUND")
