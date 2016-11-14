

result = 0

for i in range(0,1000):
    if ( 0 == i % 3 or 0 == i % 5):
        result += i

print(result)