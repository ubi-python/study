# http://euler.synap.co.kr/prob_detail.php?id=2

# 피보나치 수열

# limit = 1000
limit = 4000000

index = 0


def fibonacci_nums(start, end, odd_sum):
    print('[{}] start - {}, end - {}'.format(index, start, end))
    if end > limit:
        return odd_sum
    if end % 2 == 0:
        odd_sum += end
    return fibonacci_nums(end, start + end, odd_sum)


print(fibonacci_nums(1, 2, 0))
