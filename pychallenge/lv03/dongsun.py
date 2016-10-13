# coding=utf-8
# python challenge 3번문제

import urllib.request
import re

content = urllib.request.urlopen("http://www.pythonchallenge.com/pc/def/equality.html").read()
text = content.decode("utf-8")

# 텍스트 가져오기
textContent = text[text.find("<!--") + 5: text.find("-->")]

# print(textContent)

print(re.findall(r"[a-z]{1}[A-Z]{3}[a-z]{1}[A-Z]{3}[a-z]{1}", textContent))
arrText = re.findall(r"[a-z]{1}[A-Z]{3}[a-z]{1}[A-Z]{3}[a-z]{1}", textContent)

solution = ""

for str in arrText:
    for index in range(0, len(str)):
        if index == 0 or index == 8:
            continue
        if str[index].islower():
            solution += str[index]

# 정답 linkedlist
print(solution)
