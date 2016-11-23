num = 600851475143;
lastPrime = 0;

def isPrime(number):
    for x in range(2, number):
        if number % x == 0:
            return False
        else:
            return True
i = 2;
while i * i <= num:
    if num % i == 0:
        num = num / i
        lastPrime = num
    else:
        i += 1

print(lastPrime)
