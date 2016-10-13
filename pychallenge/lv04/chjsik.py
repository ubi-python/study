# coding=utf-8
import urllib.request

requestUrl = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=";

def getHttpContent(nothingNo):
    # print(requestUrl + nothingNo)
    content = urllib.request.urlopen(requestUrl + nothingNo).read()
    return content.decode("utf-8")

def findNextNothingNo(decodedContents, findText):
    return decodedContents[decodedContents.find(findText) + len(findText):]

findText = "and the next nothing is "
secondFindText = "Yes. Divide by two and keep going."
nothingNo = "12345"
while True:
    decodedContents = getHttpContent(nothingNo)
    # print(decodedContents)

    if findText in decodedContents:
        nothingNo = findNextNothingNo(decodedContents, findText)
    elif secondFindText == decodedContents:
        nothingNo = str(int(int(nothingNo)/2))
    else:
        print(decodedContents)
        break
