import time

start = time.time()

hailstone_sequence = 0
max_number = 1000000
result = 0
dic = dict()

# solution 1
# def getIterativeSequence(num):
#     if num % 2 == 0:
#         num /= 2
#     else:
#         num = (3 * num) + 1
#
#     return num
#
#
# for i in range(2, max_number):
#     count = 0
#     tmp = i
#     while tmp != 1:
#         count += 1
#         tmp = getIterativeSequence(tmp)
#
#     if hailstone_sequence < count:
#         hailstone_sequence = count
#         result = i

def getIterativeSequenceCount(num):
    tmp = num
    cnt = 0
    while tmp != 1:
        if i not in dic:
            if tmp % 2 == 0:
                tmp /= 2
            else:
                tmp = (3 * tmp) + 1
            cnt += 1
        else:
            cnt += (dic[i] - 1)
            break
    dic[num] = cnt

    return cnt


for i in range(2, max_number):
    count = getIterativeSequenceCount(i)

    if hailstone_sequence < count:
        hailstone_sequence = count
        result = i

print("result : [%s] elapsed [%s] seconds." % (result, (time.time() - start)))
