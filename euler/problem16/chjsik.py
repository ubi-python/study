import time
from math import factorial

start = time.time()


def getSum(num):
    result = 0
    tmp = str(num)
    for i in range(len(tmp)):
        result += int(tmp[i])
    return result


print("result : [%s] elapsed [%s] seconds." % (getSum(pow(2, 1000)), (time.time() - start)))
