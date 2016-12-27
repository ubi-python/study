"""
10.
10 이하의 소수를 모두 더하면 2 + 3 + 5 + 7 = 17 이 됩니다.

이백만(2,000,000) 이하 소수의 합은 얼마입니까?

"""
#from euler.problem7.eunsil import specialPrime
count = 9999999999999999
maxNum=2000000
"""
primeList=specialPrime(count, maxNum)
print(primeList)
sum =0
for x in primeList:
    sum+=x
print(sum)
"""

isPrimes=[]
# 0-2000000
for i in range(0,maxNum+1):
    isPrimes.append(False)
print(len(isPrimes))

resultSum =2
i=3
# 3,5,7 ... 1999999
while(True):
    if( i > maxNum):
        break
    #isPrime= True
    #for x in primes:
    #    if( i%x == 0):
    #        isPrime=False
    #        break
    #if(isPrime) :
        #primes.append(i)
        #resultSum+=i
    if( isPrimes[i] == False):
        resultSum+=i
        index = 2
        while True :
            multi = i*index
            if( multi > maxNum):
                break
            if (isPrimes[multi] == False):
                isPrimes[multi] =True
            index +=1
    i+=2

print(resultSum)