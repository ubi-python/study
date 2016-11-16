#피보나치 수열
first = 1
second = 2
sum=2
nextValue=0

while(1):
    nextValue = first + second
    if (nextValue > 4000000):
        break
    if( (nextValue % 2) == 0  ):
        sum = sum+nextValue
    first = second
    second = nextValue
print(sum)
