import math

# 소수 판별 함수
def isPrime(n):
    bPrime = True
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            bPrime = False
            break
    return bPrime


count = 0
num = 2
result = 0

while True:
    # 소수 10001번째이면 break
    if count == 10001:
        break

    # 소수인지 확인하여 맞으면 count + 1
    if isPrime(num) == True:
        count += 1
        result = num

    num += 1

print(result)
