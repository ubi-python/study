num = 2000000
result = 0;


def isPrime(number):
    for x in range(3, int(number ** 0.5 + 1), 2):
        if number % x == 0:
            return False

    return True


# solution 1
# for i in range(3, num, 2):
#     if isPrime(i):
#         result += i
# 142913828922


# solution 2
sqrt = int(num ** 0.5) + 1
prime_list = [2]
prime_result = []

for i in range(2, num + 1):
    prime_result.append(i)

for i in range(3, sqrt, 2):
    if isPrime(i):
        prime_list.append(i)

for i in range(0, len(prime_list)):
    idx = 2
    tmp = prime_list[i] * idx
    while tmp <= len(prime_result) + 1:
        prime_result[tmp - 2] = 0
        idx += 1
        tmp = prime_list[i] * idx

for i in range(len(prime_result)):
    result += prime_result[i]

print(result)
