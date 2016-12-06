def isPrime(number):
    for x in range(3, int(number ** 0.5 + 1), 2):
        if number != x and number % x == 0:
            return False

    return True


def getPrime(maxIndex):
    count = 1
    num = 3
    while True:
        if num % 2 != 0 and isPrime(num):
            count += 1

        if count == maxIndex:
            break
        else:
            num += 2

    return num;


print(getPrime(10001))
