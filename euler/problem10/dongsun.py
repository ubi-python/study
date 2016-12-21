# import math


# 소수 구하는 함수
# def isPrime(n):
#    bPrime = True
#    for i in range(2, int(math.sqrt(n)) + 1):
#        if n % i == 0:
#            bPrime = False
#            break
#    return bPrime


# result = 0

# for sosu in range(2, 2000001):
#    if isPrime(sosu):
#        result += sosu

# 142913828922
# print(result)


# 아리스토테네스 체 적용

N = 2000000

result = 0

# init
sieve = {}
for i in range(2, N + 1):
    sieve[i] = 0

# Sieve of Eratosthenes
for i in range(2, N + 1):
    if sieve[i] == 0:
        n = 2
        while i * n <= N:
            sieve[i * n] = 1
            n += 1

# print results
for i in range(2, N + 1):
    if sieve[i] == 0:
        result += i

print(result)
