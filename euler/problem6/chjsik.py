maxNum = 100
#
#
# def sumOfSquare(num):
#     result = 0
#     for i in range(1, (num+1)):
#         result += (i * i)
#     return result
#
#
# def squareOfSum(num):
#     result = 0
#     lastNum = num
#     for i in range(1, int(num / 2)+1):
#         result += (i + lastNum)
#         lastNum -= 1
#     return result * result
#
# print(squareOfSum(maxNum) - sumOfSquare(maxNum))

sumResult = 0
squareOfSumResult = 0
for i in range(1, (maxNum+1)):
    sumResult += i
    squareOfSumResult += (i * i)

print(abs(squareOfSumResult - (sumResult*sumResult)))