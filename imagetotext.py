import pytesseract
from PIL import Image, ImageEnhance, ImageFilter
import time

img = Image.open('char.jpg')

x = 90
y = 30
w = 100 + x
h = 30 + y
img1 = img.crop((x, y, w, h))
img1.save("test.jpg")

time.sleep(1)

text = pytesseract.image_to_string("test.jpg")
print(text)
