maxNumber = 4000000
result = 0
sum = 0
first = 1
second = 1


while result < maxNumber:
    if result % 2 == 0 :
        sum += result

    result = first + second
    second = first
    first = result


print(sum)
