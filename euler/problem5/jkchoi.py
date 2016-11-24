
#[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

#[2,3,5,7,11,13,17,19]
# 3 1
# 232792560


def func1(val):
    i = 2
    while ( 0 != val % i):
        i += 1
    data = [0, 0]
    data[0] = val/i
    data[1] = i
    return data


def func2(n):
    _list = [None] * 20
    i = 0
    while True:
        data = func1(n)
        _list[i] = data[1]
        i += 1
        if (1 == data[0]):
            break;
        n = data[0]
    return _list

list = [None] * 20
i = 0
for n in range(2,21):
    l = func2(n)
    for k in l:
        if ( k == None):
            continue
        while ( list.count(k) < l.count(k) ):
            list[i] = k
            i += 1

result =1
for p in list:
    if ( p == None ):
        continue
    result *= p

print(result)

# -> 232792560