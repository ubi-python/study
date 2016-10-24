# coding=utf-8
import urllib.request
import pickle
import sys

requestUrl = "http://www.pythonchallenge.com/pc/def/banner.p"
data = urllib.request.urlopen(requestUrl).read()
tmp = pickle.loads(data)

# print(tmp)

result = ""
for list in tmp:
    for varTuple in list:
        for index in range(0, varTuple[1]):
            result += varTuple[0]
    result += "\n"

# channel
print(result)
