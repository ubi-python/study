divisorCount = 500


def getTriangleNumber(num, addNum):
    # val = 0
    # for i in range(1, num + 1):
    #     val += i
    #
    # return val
    # return int(num * (num + 1) / 2)
    return num + addNum


def getDivisors(num):
    # i = 1
    # cnt = 0
    # while (i * i) <= num:
    #     if num % i == 0:
    #         cnt += 2
    #     i += 1
    #
    # return cnt
    i = 2
    cnt = 1
    tmp = num
    while i <= tmp:
        if tmp % i == 0:
            j = 0
            while tmp % i == 0:
                tmp = tmp / i
                j += 1

            cnt = cnt * (j + 1)

        i += 1

    return cnt


start = 1
result = 0
while True:
    result = getTriangleNumber(result, start)
    if divisorCount < getDivisors(result):
        break
    else:
        start += 1

print(result)
