def factorial(num):
    if num == 1 or num < 1:
        return num
    return num * factorial(num - 1)


print('한글')
print ('Welcome to Ubivelox Python Study!!!')


result = factorial(8)
print(result)
