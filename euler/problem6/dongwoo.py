sumValue = 0
powValue = 0

for i in range(1,101):
    sumValue+=i
    powValue+= pow(i, 2)

sumValue = pow(sumValue, 2)
print(sumValue - powValue)