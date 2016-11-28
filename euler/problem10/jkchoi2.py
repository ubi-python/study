testNo = 2000000

list1 = range(0, testNo)
list2 = [False]+[False]+[True] * (testNo-1)

for n in list1:
    if ( False == list2[n] ):
        continue

    val = n+n
    if ( val > testNo):
        continue

    while True:
        list2[val] = False
        val += n
        if ( val > testNo):
            break


result = 0
for i in range(len(list2)):
    if ( list2[i] ):
        result += i

print(result)
