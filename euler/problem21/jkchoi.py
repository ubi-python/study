ndict = {}

def getDivisors(_n):
    list = []

    for i in range(_n, 0, -1):
        if (1 == i or _n == i):
            if ( i not in list):
                list.append(i)
                continue

        if ( i in list):
            continue

        if ( 0 == _n % i):
            if (i in ndict):
                for j in ndict.get(i):
                    if ( j not in list):
                        list.append(j)
            else:
                if (i not in list):
                    list.append(i)

    ndict[_n] = list
    return list

def getSum(_l):
    result = 0
    for v in _l:
        result += v

    return result


results  = []
for i in range(1, 10001):
    l1 = getDivisors(i)
    s1 = getSum(l1) - i
    l2 = getDivisors(s1)
    s2 = getSum(l2) - s1

    if ( i != s1 and i == s2 and i not in results):
        print("amicable number : " + str(i) + ", " + str(s1))
        results.append(i)
        results.append(s1)


sum = 0
for val in results:
    sum += val

print(sum)