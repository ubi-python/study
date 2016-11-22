# coding=utf-8

first = 1
second = 2
result = 0
sum = 2
maxNum = 4000000

while True:

    if result > maxNum:
        break

    result = first + second

    if result % 2 == 0:
        sum += result

    first = second
    second = result

# 4613732
print(sum)
