a = 0
for i in range(1, 1000):
    if (i % 3 == 0) | (i % 5 == 0):
        a = a + i
print(a)