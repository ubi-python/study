'''
    for n in range(2, limit):
        while num % n == 0:
            num = num / n
            answer = n
            print('{}/{} = {}'.format(num * n, n, num))
        if num == 1:
            break
        n += 1
'''
sum_num = 0
prime_num_list = [2]


def decide_prime_number(q_num, prime_numbers):
    for p in prime_numbers:
        if q_num != p and q_num % p == 0:
            return False
    return True


# limit = 2000000
limit = 2000000
cnt = 2
while cnt < limit:
    if decide_prime_number(cnt, prime_num_list):
        # print('{}'.format(cnt), end=' , ')
        sum_num += cnt
        prime_num_list.append(cnt)
    cnt += 1
print()
print("답 : ", sum_num)
