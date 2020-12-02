import pytesseract
from PIL import Image, ImageEnhance, ImageFilter
import time

img = Image.open('/home/sean/Pictures/Capture/capture000006.jpg')

# x = 1800
# y = 500
# w = 1000 + x
# h = 200 + y
x = 3150
y = 3030
w = 300 + x
h = 50 + y
img1 = img.crop((x, y, w, h))
img1.save("pokemon/test.jpg")

time.sleep(1)

text = pytesseract.image_to_string(
    "pokemon/test.jpg", lang="eng", config="--psm 7")
print(text)
