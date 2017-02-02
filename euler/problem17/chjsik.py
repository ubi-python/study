import time
import inflect

start = time.time()


def getSum():
    sumPosition = 0
    for idx in range(1, 1001):
        p = inflect.engine()
        sumPosition += len(p.number_to_words(idx).replace("-", "").replace(" ", ""))
    return sumPosition


print("result : [%s] elapsed [%s] seconds." % (getSum(), (time.time() - start)))
