import urllib.request
import collections
import re

content = urllib.request.urlopen("http://www.pythonchallenge.com/pc/def/equality.html").read()

#print(content)
#print(type(content))

text = content.decode("utf-8")

ex = text[text.find("<!--") + 5 : text.rfind("-->") - len(text)]

print("".join(re.findall("[^A-Z]+[A-Z]{3}([a-z])[A-Z]{3}[^A-Z]+", ex)))