"""
http://euler.synap.co.kr/prob_detail.php?id=7

소수를 크기 순으로 나열하면 2, 3, 5, 7, 11, 13, ... 과 같이 됩니다.

이 때 10,001번째의 소수를 구하세요.

소수 : prime
"""

# 소수 확인하는 함수
def prime(number):

    isPrime = True

    for i in range (2,number,1):

        # 나누어 떨어지는 수가 있으면 소수가 아님
        if number % i == 0 :
            return False

    # 나누어 떨어지는 수가 없으면 소수 임
    return isPrime

# 소수 저장 리스트
sosuList = []

value = 1
while True:
    #값 증가
    value+= 1

    # 소수이면 리스트에 추가
    if(prime(value)):
        sosuList.append(value)

    if(len(sosuList) >= 10001) :
        break

print (max(sosuList))

# 104743