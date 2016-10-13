import urllib.request
import collections

content = urllib.request.urlopen("http://www.pythonchallenge.com/pc/def/equality.html").read()

#print(content)
#print(type(content))

text = content.decode("utf-8")

ex = text[text.find("<!--") + 5 : text.rfind("-->") - len(text)]
#print (ex)

#print(ord("A"))
#print(ord("Z"))
#print(ord("a"))
#print(ord("z"))

def isCapital(_c):
    return (65 <= ord(_c) <= 90)

def isSmall(_s):
    return (97 <= ord(_s) <= 122)

tLen = len(ex)
result = ""
for i in range(0, tLen):
    if ( i < 4 ):
        continue

    if ( i + 4 > tLen - 1) :
        break

    if ( isSmall(ex[i - 4]) &
         isCapital(ex[i - 3]) &
         isCapital(ex[i - 2]) &
         isCapital(ex[i - 1]) &
         isSmall(ex[i]) &
         isCapital(ex[i + 1]) &
         isCapital(ex[i + 2]) &
         isCapital(ex[i + 3]) &
         isSmall(ex[i + 4]) ):
        result += ex[i]

print(result)


