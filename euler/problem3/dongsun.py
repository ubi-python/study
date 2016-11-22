inVal = 600851475143
# 소인수 분해하기
dvide = 2

#딕셔너리 선언
result = dict()

while True:

    # 나머지가 0인 경우
    if (inVal % dvide == 0):

        # inVal 값을 divde로 나눔.
        inVal = inVal / dvide

        # 딕셔너리에 key가 존재하는지 확인.
        if dvide in result:
            result[dvide] = result[dvide] + 1
        else:
            result[dvide] = 1
        # 딕셔너리 입력 후 다시 2로 값 초기화
        dvide = 2

    else:
        # 나머지가 0이 아니면 나눌 몫을 1 증가
        dvide = dvide + 1

        # 나눌 값 (inVal)이 나눌 몫 값(divide)가 같아지면 중지
        if inVal == dvide:
            # 딕셔너리에 key가 존재하는지 확인.
            if dvide in result:
                result[dvide] = result[dvide] + 1
            else:
                result[dvide] = 1
            break

# {6857: 1, 839: 1, 1471: 1, 71: 1}
print(result)
