


n = 1000
result = 1

for i in range(0,n):
    result *= 2

print(result)

sum = 0
data = str(result)
for i in range(0, len(data)):
    sum += int(data[i])

print(sum)