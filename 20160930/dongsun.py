# coding=utf-8
# 1번 문제 : 2의 38 값 구하기

result = pow(2, 38)
print(result)

# 2의 38 값 = 274877906944

# 2번 문제

inputText = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

outputText = ""

for i in range(0, len(inputText)):

    if 97 <= ord(inputText[i]) <= 120:  # a~x 문자 변경
        outputText += chr(ord(inputText[i]) + 2)
    elif ord(inputText[i]) == 121 or ord(inputText[i]) == 122:  # y->a or z->b로 변경
        outputText += chr(ord(inputText[i]) + 2 - 26)
    else:
        outputText += inputText[i]

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
