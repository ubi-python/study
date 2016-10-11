# coding=utf-8
# python challenge 2번문제

import urllib.request
import collections

content = urllib.request.urlopen("http://www.pythonchallenge.com/pc/def/ocr.html").read()
text = content.decode("utf-8")
# 텍스트 가져오기
ex = text[text.find("<!--", text.find("<!--") + 1) + 5: text.rfind("-->") - len(text)]

dict = collections.OrderedDict()

for chr in ex:
    if chr in dict.keys():
        dict[chr] += 1
    else:
        dict[chr] = 1

soltuion = ""

for key in dict:
    if dict.get(key) == 1:
        soltuion += key

# 답 : equality
print(soltuion)
