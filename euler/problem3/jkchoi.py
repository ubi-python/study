def func(val):
    i = 2
    while ( 0 != val % i):
        i += 1
    data = [0, 0]
    data[0] = val/i
    data[1] = i
    return data


n = 600851475143

while True:
    data = func(n)
    print(data)
    if (1 == data[0]):
        break;

    n = data[0]
