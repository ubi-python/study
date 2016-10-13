import urllib.request
import urllib.parse
import re
import random


def getContext(num):
    params = urllib.parse.urlencode({'nothing':  str(num)})
    f = urllib.request.urlopen("http://www.pythonchallenge.com/pc/def/linkedlist.php?%s" % params)
    context = f.read()
    print((context))
    a = re.findall("[0-9]{1,5}", str(context))
    print(a)
    indexOfText=len(a) -1
    return str(a[indexOfText])

randomnumber = "12345"
for i in range(400):
    try:
        print(i)
        randomnumber=getContext(randomnumber)
    except Exception:
        break

intRandomnumber = int(int(randomnumber) / 2)
print(intRandomnumber)
randomnumber = getContext(intRandomnumber)

while(1):
    try:
        print(randomnumber)
        randomnumber = getContext(randomnumber)
    except Exception:
        break

print("end")