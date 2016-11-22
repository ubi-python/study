"""
1 ~ 10 사이의 어떤 수로도 나누어 떨어지는 가장 작은 수는 2520입니다.
그러면 1 ~ 20 사이의 어떤 수로도 나누어 떨어지는 가장 작은 수는 얼마입니까?
"""

# 초기값 지정
value = 2500
# 발견여부
correct = False

#반복시작
while 1:

    # 반복 종료 조건 : 값 찾을 경우
    if correct == True :
        print("answer : ", value)
        break

    # 값 증가
    value += 1

    # 1,000,000 단위 마다 화면 표시
    if value % 1000000 == 0 :
        print ("now checking value : %d"  %value)

    # 1부터 20까지 나눔
    for i in range(1,21):

        #print(value, i, value%i)

        # 만일 나머지가 0이 아닐경우 반복 중지
        if value % i != 0 :
            break

        # 20까지 나누어도 break 되지 않았다면 값 찾음
        if i== 20 :
            correct = True



# 한참 걸린 후 결과값 나옴
# 232792560
