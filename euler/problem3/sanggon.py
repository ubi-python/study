# input_num = 12345678
input_num = 600851475143


# 1. 1과 주어진 숫자 사이에 있는 소수를 찾아라
#   소수 : 소인수분해했을 때 인수가 1과 자기자신 밖에 없는 것
# 2.


def search_prime_number(limit):
    answer = 0
    num = int(limit)
    for n in range(2, limit):
        while num % n == 0:
            num = num / n
            answer = n
            print('{}/{} = {}'.format(num * n, n, num))
        if num == 1:
            break
        n += 1
    return answer


an = search_prime_number(input_num)

print('답 : {}'.format(an))
