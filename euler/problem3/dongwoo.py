def getMinimumPrime(value):
    if 2 == value:
        return value
    for i in range(2, value):
        if value%i == 0:
            return i
    return value




value = 600851475143
while(True):
    prime = getMinimumPrime(value)
    print(prime)
    value = int(value/prime)
    if (value == 1):
        break