def reverse(txt):
    return txt[::-1]

startNumber = 100
endNumber = 999
result = 0

for i in range(startNumber, endNumber):
    for j in range(startNumber, endNumber):
        multiply = i * j
        if str(multiply) == reverse(str(multiply)) and result < multiply:
            result = multiply

print(result)

