endNumber = 1000
result = 0;

for i in range(endNumber):
    if i % 3 == 0 or i % 5 == 0:
        result += i

print(result)
