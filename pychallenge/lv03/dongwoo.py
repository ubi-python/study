# coding=utf-8

import urllib.request
import re

content = urllib.request.urlopen("http://www.pythonchallenge.com/pc/def/equality.html").read()
text = content.decode("utf-8")
#print(text)

# 텍스트 가져오기
textContent = text[text.find("<!--") + 5: text.find("-->")]
#print(textContent)

result = "".join(re.findall('[a-z][A-Z]{3}([a-z])[A-Z]{3}[a-z]', textContent))
print(result)


