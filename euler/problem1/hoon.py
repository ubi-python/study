"""
1000 보다 작은 자연수 중에서 3또는 5의 배수를 모두 더하면 얼마 일까요?
"""
sum = 0
# 1부터 1000까지 루프
for i in range(1,1000) :
    if(i % 3 == 0 or i % 5 == 0) :
        # print(i)
        sum += i

print(sum)




