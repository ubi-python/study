import time

start = time.time()

hailstone_sequence = 0
max_number = 1000000
result = 0


def getIterativeSequence(num):
    if num % 2 == 0:
        num /= 2
    else:
        num = (3 * num) + 1

    return num


for i in range(2, max_number):
    count = 0
    tmp = i
    while tmp != 1:
        count += 1
        tmp = getIterativeSequence(tmp)

    if hailstone_sequence < count:
        hailstone_sequence = count
        result = i

print("result : [%s] in [%s] seconds." % (result, (time.time() - start)))