
list = []




i = 1
j = 1

list.append(i)
list.append(j)

result = 0
while True:
    k = i + j
    list.append(k)
    i = j
    j = k
    if ( 1000 <= len(str(k)) ):
        result = len(list)
        break


print(result)