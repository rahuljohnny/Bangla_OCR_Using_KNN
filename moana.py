
'''
import pytesseract
from PIL import Image
print pytesseract.image_to_string(Image.open("ACCURACY\\type4_0.jpg"))
'''

import pytesseract
from PIL import Image

img = Image.open('pyt.jpg')
img.load()
i = pytesseract.image_to_string(img)
print i
print"==========================================="

print(pytesseract.image_to_string(img, lang='ben'))
