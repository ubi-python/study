# 문제 6번

import math

pow_sum = 0
normal_sum = 0
for x in range(1, 101):
    normal_sum = normal_sum + x
    pow_sum += math.pow(x, 2)

normal_sum = math.pow(normal_sum, 2)
print("{} - {} = {}".format(normal_sum, pow_sum, abs(normal_sum - pow_sum)))
