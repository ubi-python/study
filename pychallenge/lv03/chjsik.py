# coding=utf-8
import urllib.request
import re

htmlContent = urllib.request.urlopen("http://www.pythonchallenge.com/pc/def/equality.html").read()

decodedContents = htmlContent.decode("utf-8")

# print(decodedContents)

splitedList = decodedContents.split("<!--\n")
# print(splitedList[1])

p = re.compile("[a-z][A-Z]{3}[a-z][A-Z]{3}[a-z]")
regList = p.findall(splitedList[1])

result = ""
for str in regList:
    result += str[4:5]

print(result)
