sum = 1000

def isInt(i):
    if int(i) == i:
        return True
    else:
        return False

def calc():
    for i in range(1, sum):
        for j in range(i + 1, sum):
            c = (i ** 2 + j ** 2) ** 0.5
            if isInt(c):
                if i + j + int(c) == sum:
                    return i * j * c
    return 0

print(calc())
