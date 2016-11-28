
def isPrime(val):
    i = 2
    while ( 0 != val % i):
        i += 1
    if (i == val):
        return True
    return False


result = 0
for i in range(2, 2000000):

    if ( 0 == i%10000):
        print("progress : " + str(i))

    if ( isPrime(i)):
        result += i

print(result)