"""
피보나치 수열의 각 항은 바로 앞의 항 두 개를 더한 것이 됩니다. 1과 2로 시작하는 경우 이 수열은 아래와 같습니다.

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

짝수이면서 4백만 이하인 모든 항을 더하면 얼마가 됩니까?

"""

check = 0
hang01 = 1
hang02 = 2
result = 2  # 루프 상 초기 값 검증이 없어 미리 반영 함

# 검증 값이 4백만 이하까지만 반복
while check <= 4000000 :

    # 항두개를 합쳐서 검증
    check = hang01 + hang02

    # 짝수 이면 더함
    if check % 2 == 0 :
        result += check

    # 두개의 항 값을 바꿈
    hang01 = hang02
    hang02 = check

    print(hang01, hang02, result)

print(result)

# 4613732






