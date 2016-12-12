value = 1000

# a의 최대 수는 332
for a in range(1, int(value/3-1)):
    # b의 최대 수는 499
    for b in range(a + 1, int(value-a/2)):
        c = 1000 - (a+b)
        if a + b + c == value and pow(a, 2) + pow(b, 2) == pow(c, 2):
            print("a : ", a)
            print("b : ", b)
            print("c : ", c)
            print("a * b * c : ", a * b * c)

