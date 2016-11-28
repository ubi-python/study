result = 2


def gcd(a, b):
    while b != 0:
        remainder = a % b
        a = b
        b = remainder
    return abs(a)


def lcm(a, b):
    return abs((a * b) / gcd(a, b))


for i in range(2, 20):
    result = lcm(result, i + 1)

print(result)
