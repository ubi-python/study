# coding=utf-8
# 2번 문제

inputText = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

outputText = ""

for i in inputText:

    if not i.isalpha():
        outputText += i

    elif ord(i) < 121:
        outputText += chr(ord(i) + 2)
    else:
        outputText += chr(ord(i) + 2 - 26)

# 변경 문자열 출력
print(outputText)

# 정답 후 maketrans 사용법 적용
inTab = "abcdefghijklmnopqrstuvwxyz"
outTab = "cdefghijklmnopqrstuvwxyzab"
transMap = str.maketrans(inTab, outTab)
print(inputText.translate(transMap))

# 정답에 넣을 url 주소
inUrl = "map"
print(inUrl.translate(transMap))  # map > ocr
