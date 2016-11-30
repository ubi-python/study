
#제곱의 합
sumOfPow = 0
#합의 제곱
powOfSum = 0

for index in range(1, 101) :
    powOfSum += index
    sumOfPow += pow(index, 2)

powOfSum = pow(powOfSum, 2)

result = powOfSum - sumOfPow

# 25502500 : 합의 제곱
print(powOfSum)
# 338350 : 제곱의 합
print(sumOfPow)
# 25164150 : 합의 제곱 - 제곱의 합
print(result)

