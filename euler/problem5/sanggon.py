start_num = 2


def gcd(a, b):
    while b != 0:
        remainder = a % b
        a = b
        b = remainder

    return a


def lcm(a, b):
    return (a * b) / gcd(a, b)


for i in range(2, 20):
    start_num = lcm(start_num, i + 1)

print("답 : {}".format(start_num))
