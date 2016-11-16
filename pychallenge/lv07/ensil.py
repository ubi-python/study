import urllib.request
from PIL import Image

urllib.request.urlretrieve('http://www.pythonchallenge.com/pc/def/oxygen.png', 'oxygen_ES.png')
f = open('oxygen_ES.png', 'wb')
i=Image.open('oxygen_ES.png')
print(f)

