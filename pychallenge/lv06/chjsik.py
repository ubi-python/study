# coding=utf-8
import urllib.request
import zipfile

filePath = "D:\\download\\channel\\"
fileName = "90052"
fileExtension = ".txt"


def getFileContent(fileName):
    # print(requestUrl + nothingNo)
    f = open(filePath + fileName + fileExtension)
    return f.readline()


def findNextNothingNo(fileContents, findText):
    return fileContents[fileContents.find(findText) + len(findText):]


findText = "Next nothing is "
secondFindText = "Collect the comments."
zf = zipfile.ZipFile("channel.zip")
result = ""

while True:
    fileContents = getFileContent(fileName)
    # print(fileContents)

    if findText in fileContents:
        fileName = findNextNothingNo(fileContents, findText)
        comment = zf.getinfo(fileName + fileExtension).comment
        result += comment.decode("utf-8")
    else:
        # print(fileContents)
        break

print(result)
