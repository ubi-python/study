# coding=utf-8
import urllib.request
import pickle

requestUrl = "http://www.pythonchallenge.com/pc/def/banner.p"
data = urllib.request.urlopen(requestUrl).read()
print(type(data))

tmp = pickle.loads(data)
# print(tmp)

for str in tmp:
    # print(str)
    line = ""
    for str1 in str:
        # print(str1)
        for str2 in range(0, str1[1]):
            line += str1[0]
    print(line)

