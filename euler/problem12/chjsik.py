divisorCount = 500


def getTriangleNumber(num):
    val = 0
    for i in range(1, num + 1):
        val += i

    return val


def getDivisors(num):
    i = 1
    cnt = 0
    while (i * i) <= num:
        if num % i == 0:
            cnt += 1
            tmp = int(num / i)
            if i == tmp:
                break
            cnt += 1
        i += 1

    return cnt


start = 1
result = 0
while True:
    result = getTriangleNumber(start)
    if divisorCount < getDivisors(result):
        break
    else:
        start += 1

print(result)
