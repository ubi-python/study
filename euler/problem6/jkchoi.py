
def func(_n):
    r1 = 0
    r2 = 0

    for i in range(1, _n+1):
        r1 += (i*i)
        r2 += i

    r2 *= r2

    return r2 - r1

d = func(100)
print(d)