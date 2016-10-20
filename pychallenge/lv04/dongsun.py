# coding=utf-8

import urllib.request

inData = "44827"

for index in range(0, 400):
    req_url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=" + inData
    req = urllib.request.Request(req_url)
    data = urllib.request.urlopen(req).read()
    print(data)
    text = str(data)

    if text.rfind("is") > 0:
        inData = text[text.rfind("is") + 3:len(text) - 1]
    elif text.rfind("Divide") > 0:
        inData = str(int(inData) / 2)
    else:
        break

# peak.html
