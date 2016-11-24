def func(val):
    i = 2
    while ( 0 != val % i):
        i += 1
    if (i == val):
        return True
    return False

i = 2
count = 0
while True:
    if ( func(i) ):
        count += 1
        #print(count)
        if ( 10001 == count):
            print(i)
            break

    i += 1
