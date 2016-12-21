#소수를 크기 순으로 나열하면 2, 3, 5, 7, 11, 13, ... 과 같이 됩니다.
#이 때 10001번째의 소수를 구하세요.
import math

def isPrime(num):
    for i in range(2, num):
        if num%i == 0:
            return False
    return True

def isPrime2(n):

    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True

number = 2
count = 0
while(True):
    if isPrime(number):
        print(number)
        count+=1
        if count == 10001:
            print(number)
            break
    number+=1
