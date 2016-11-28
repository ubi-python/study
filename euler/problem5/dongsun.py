import math


# 소수 구하는 함수
def isPrime(n):
    bPrime = True
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            bPrime = False
            break
    return bPrime


# 딕셔너리 선언
resultDict = dict()
result = 1

# 소수 및 소수가 몇번 호출됬는지 구하여 딕셔너리에 넣어줌.
for index in range(2, 20):
    num = 19

    while True:

        if num < index or isPrime(index) == False:
            break

        num = num / index

        # 딕셔너리에 key가 존재하는지 확인.
        if index in resultDict:
            resultDict[index] = resultDict[index] + 1
        else:
            resultDict[index] = 1

# 딕셔너리 출력
# {19: 1, 17: 1, 2: 4, 3: 2, 5: 1, 7: 1, 11: 1, 13: 1}
print(resultDict)

# 딕셔너리에 있는 데이터를 모두 곱합.
for key in resultDict.keys():
    result *= pow(key, resultDict[key])

#232792560
print(result)
