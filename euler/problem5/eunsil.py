"""
1 ~ 10 사이의 어떤 수로도 나누어 떨어지는 가장 작은 수는 2520입니다.

그러면 1 ~ 20 사이의 어떤 수로도 나누어 떨어지는 가장 작은 수는 얼마입니까?
"""

allSet = {}

for i in range(1,20):
    x =2
    temp = i
    current={}
    if(temp<=x):
        current[temp] = 1
    else:
        while(True):
            if( temp%x ==0):
                temp =temp/x
                if x in current:
                    current[x] = current[x] + 1
                else:
                    current[x] =1
                x=1
            if(temp == 1):
                break
            x= x+1

    for tt in current:
        if tt in allSet:
            if allSet[tt] < current[tt]:
                allSet[tt] = current[tt]
        else:
            allSet[tt] = current[tt]


#print('1' in allSet)
print(allSet)
result = 1
for yy in allSet:
    result = result * ( pow( yy , allSet[yy]))
    print(result)
print(result)