"""
문제)
1부터 n까지의 자연수를 차례로 더하여 구해진 값을 삼각수라고 합니다.
예를 들어 7번째 삼각수는 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28이 됩니다.
이런 식으로 삼각수를 구해 나가면 다음과 같습니다.

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

이 삼각수들의 약수를 구해봅시다.

 1: 1
 3: 1, 3
 6: 1, 2, 3, 6
10: 1, 2, 5, 10
15: 1, 3, 5, 15
21: 1, 3, 7, 21
28: 1, 2, 4, 7, 14, 28

위에서 보듯이, 5개 이상의 약수를 갖는 첫번째 삼각수는 28입니다.

그러면 500개 이상의 약수를 갖는 가장 작은 삼각수는 얼마입니까?

방법)
1. 자연수를 차례로 더해가며 삼각수를 구한다.
2. 새로운 삼각수의 약수를 구한다.
3. 약수의 갯수가 500개 이상이면 해당 삼각수가 답이다.
"""
# 약수구하기 함수
def yak_count(number):
    count = 0
    first = 1
    second = number
    while first < second:

        if number%first == 0:
            second = int(number/first)
            if first == second:
                count += 1
            else:
                count += 2 #약수 2개추가

        first += 1

    print(number, count)


    return count

# 자연수
n = 0
# 삼각수
s = 0
while True:
    n += 1
    s += n

    if yak_count(s) >= 500:
        print("# 답 : ", s)
        break


# 답 :  76576500