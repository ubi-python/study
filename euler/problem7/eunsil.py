"""
7
소수를 크기 순으로 나열하면 2, 3, 5, 7, 11, 13, ... 과 같이 됩니다.

이 때 10,001번째의 소수를 구하세요.
"""

"""
오래걸림.

limitIndex = 10001
count=0
currentNum=2
while(True):
    divisor = 2
    while(True):
        if(currentNum%divisor ==0):
            if(currentNum == divisor):
                print(currentNum)
                count +=1
                break
            else:
                break
        divisor += 1
    if (count == limitIndex):
        print(currentNum)
        break
    currentNum += 1

"""
"""
에라토스테네스의 체 이용
"""
primeList =[ 3, 5]
mutiCounter=[2,2]
limitCount = 10001
buff=0

startNum=2
endNum =2
while(True):
    if(len(primeList) >= limitCount-1):
        print(primeList[ limitCount-2])  #2를 제외 시켰기 때문에 10000번째(0-9999) 소수를 출력
        break
    endNum = primeList[len(primeList)-1] * primeList[len(primeList)-1]
    if(endNum > limitCount):
        buff += 1000
        endNum = limitCount+buff

    numlist = []
    for x in range(startNum, endNum+1):
        if not ( x%2==0):
            numlist.append(x)

    print(endNum)
    count = 0
    for i in primeList:
        #temp = i * startNum
        while( True):
            temp = i* mutiCounter[count]
            if temp in numlist:
                numlist.remove(temp)
            if(  temp >= endNum ):
                break
            mutiCounter[count]+=1
        count +=1

    for i in numlist:
        if not i in primeList:
            primeList.append(i)
            mutiCounter.append(2)

    startNum = endNum
    print(len(primeList))

