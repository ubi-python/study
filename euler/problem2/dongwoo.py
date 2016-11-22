
first = 1;
second = 2;
sum = 0;
total = 2;

while True:
    if(sum > 4000000 ):
        break
    sum = first + second
    if ( sum%2 == 0 ):
        total += sum
    first = second
    second = sum


print(total)