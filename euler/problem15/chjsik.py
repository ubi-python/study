import time
from math import factorial

start = time.time()


def getFactorial(num):
    if num == 1:
        return 1
    return num*getFactorial(num - 1)


def getCombination(n, r):
    return getFactorial(n) / (getFactorial(r) * getFactorial(n - r))

# def getCombination(n, r):
#     return factorial(n) / (factorial(r) * factorial(n - r))

print("result : [%s] elapsed [%s] seconds." % (getCombination(40, 20), (time.time() - start)))
