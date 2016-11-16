

i = 1
j = 2

sum = j
while (j < 4000000):
    next = i + j
    if ( 0 == next % 2) :
        sum += next
    i = j
    j = next

print(sum)