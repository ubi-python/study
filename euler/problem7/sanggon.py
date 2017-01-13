# q7

'''
소수를 크기 순으로 나열하면 2, 3, 5, 7, 11, 13, ... 과 같이 됩니다.
이 때 10,001번째의 소수를 구하세요.
'''

base_prime_num = list()
base_prime_num.append(2)

perf_count = 0

def is_divide_by_prime_num(num):
    for x in base_prime_num:
        if num % x == 0:
            return True
    return False


def is_prime_num(num, base):
    while base != num:
        if num % base == 0:
            return False
        else:
            base += 1
    return True


def count_prime_num(start, question):
    count = 1
    max_prime_num = 1
    while count != question:
        if not is_divide_by_prime_num(start):
            if is_prime_num(start, max_prime_num + 1):
                count += 1
                max_prime_num = start
                base_prime_num.append(max_prime_num)
                #                print("소수 개수 : ", count, ", max : ", max_prime_num)
        start += 1

    return base_prime_num[-1]


answer = count_prime_num(2, 10001)
print("답 : {}".format(answer))
