

def fact(_n):
    result = 1

    for i in range(1, _n):
        result *= i

    return result


val = str(fact(100))
sum = 0

for l in range(0, len(val)):
    sum += int(val[l])

print(sum)