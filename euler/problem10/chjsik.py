num = 2000000
result = 2;

def isPrime(number):
    for x in range(3, int(number ** 0.5 + 1), 2):
        if number != x and number % x == 0:
            return False

    return True


for i in range(3, num):
    if (i % 2) != 0 and isPrime(i):
        result += i

print(result)
