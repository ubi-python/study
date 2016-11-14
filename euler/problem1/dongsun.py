# coding=utf-8
inputVal = int(input("숫자를 입력해주세요:"))

outputVal = 0

for index in range(0, inputVal):
    if index % 3 == 0 or index % 5 == 0:
        outputVal += index

# 233168
print(outputVal)
