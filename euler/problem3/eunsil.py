"""
어떤 수를 소수의 곱으로만 나타내는 것을 소인수분해라 하고, 이 소수들을 그 수의 소인수라고 합니다.
예를 들면 13195의 소인수는 5, 7, 13, 29 입니다.

600851475143의 소인수 중에서 가장 큰 수를 구하세요.
"""
def isPrimeDivisor( paramNum):
    isPrimeDivisorBool = True
    if( 0< paramNum <=2):
        isPrimeDivisorBool=True
    else:
        for divisorNum in range(2,paramNum-1):
            if( paramNum %divisorNum ==0):
                isPrimeDivisorBool=False
                break
    return  isPrimeDivisorBool


"""
originalNum = 600851475143
maxNum = originalNum
while( originalNum >0):
    print(maxNum)
    if( originalNum % maxNum ==0):
        if( isPrimeDivisor(maxNum) ):
            break
    maxNum= maxNum-1
    print(maxNum)

print(maxNum)

"""

originalNum = 600851475143
maxNum = 0
tempDivisor =2
while( originalNum >0):
    if( originalNum % tempDivisor ==0):
        print("tempDivisor:"+ str(tempDivisor))
        if( isPrimeDivisor(maxNum) ):
            originalNum = originalNum/tempDivisor
            if( maxNum < tempDivisor):
                maxNum = tempDivisor
                tempDivisor= 1
        if(originalNum == tempDivisor):
            print("tempDivisor:" +  str(tempDivisor) +"originalNum:"+  str(originalNum))
            break
    tempDivisor= tempDivisor+1
    print("originalNum:"+  str(originalNum))

print(maxNum)
"""
 originalNum == 1 이면 끝내도 될듯
"""











