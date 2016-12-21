

def getFactorCount(_n):
    if (1 == _n):
        return 1

    list = [1] + [_n]
    n1 = 2
    while True:
        if n1 in list:
            break;

        if (0 == _n % n1):
            list.append(n1)
            list.append(_n/n1)
        n1 += 1
    return len(list)

n1 = 1
n2 = 1
while True:
    result = getFactorCount(n1)
    print(str(n1) + " : " + str(getFactorCount(n1)))
    if ( result > 500 ):
        print ("!!!!!!!!!!!!!! " + str(n1) + " : " + str(getFactorCount(n1)))
        break;

    n1 += (n2 + 1)
    n2 += 1

