# 1000보다 작은 자연수 중에서 3 또는 5의 배수를 모두 더하기
sum=0
for index in range(0,1000):
    if( index %3 == 0 or index %5==0):
        sum= sum+index
print(sum)