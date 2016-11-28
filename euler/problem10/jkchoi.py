_list = []

def isPrime(val):
    for n in _list:
        if ( 0 == val % n):
            return False

    return True

result = 0
for i in range(2, 2000000):

    if ( 0 == i%10000):
        print("progress : " + str(i))

    if ( isPrime(i)):
        _list.append(i)
        result += i

print(result)