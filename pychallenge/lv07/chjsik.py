# coding=utf-8

import urllib.request
from PIL import Image

requestUrl = "http://www.pythonchallenge.com/pc/def/oxygen.png"
data = urllib.request.urlopen(requestUrl).read()
print(data)

img = Image.open('oxygen.png')
print(img.size)
print(img.mode)

pix = img.load()
print(img.size)  # Get the width and hight of the image for iterating over
print(pix)  # Get the RGBA Value of the a pixel of an image

width = img.size[0]
height = img.size[1] / 2
text = ""

for x in range(0, width, 7):
    out = img.getpixel((x, height))
    text += chr(out[0])

print(text)

startIdx = text.find('[')
endIdx = text.find(']')
text1 = text[startIdx + 1: endIdx]

print(text1)

splitedText = text1.split(",")
result = ""
for charater in splitedText:
    result += chr(int(charater))

print(result)
