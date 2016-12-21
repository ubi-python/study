#1 ~ 10 사이의 어떤 수로도 나누어 떨어지는 가장 작은 수는 2520입니다.
#그러면 1 ~ 20 사이의 어떤 수로도 나누어 떨어지는 가장 작은 수는 얼마입니까?


def getMinimumPrime(value):
    if 2 == value:
        return value
    for i in range(2, value):
        if value%i == 0:
            return i
    return value


dic2 = {}
for i in range(2,20):
    dic = {}
    value = i
    while(True):
        prime = getMinimumPrime(value)
        if prime in dic:
            dic[prime] = dic[prime] * prime
        else:
            dic[prime] = prime
        value = int(value/prime)
        if (value == 1):
            break

    if len(dic2) == 0:
        dic2 = dic
    else:
        for key in dic.keys():
            if key in dic2:
                if ( dic[key] > dic2[key]):
                    dic2[key] = dic[key]
            else:
                dic2[key] = dic[key]

sum = 1
for value in dic2.values():
    sum*=value

print(sum)


