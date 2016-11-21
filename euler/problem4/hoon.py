"""
앞에서부터 읽을 때나 뒤에서부터 읽을 때나 모양이 같은 수를 대칭수(palindrome)라고 부릅니다.

두 자리 수를 곱해 만들 수 있는 대칭수 중 가장 큰 수는 9009 (= 91 × 99) 입니다.

세 자리 수를 곱해 만들 수 있는 가장 큰 대칭수는 얼마입니까?
"""

# 999 * 999 부터 하나씩 내려가면서 곱의 수를 구한다.
# 결과 값을 뒤집었을 때와 같은지 비교한다.
# 같은 값이 나오면 중지한다.
# 문자열 반전은 reverse() 사용

# 문자열 반전 함수
def reserse_txt(text) :
    reserve_text = ""
    text_len = len(text)
    for i in text:
        reserve_text += text[text_len-1]
        text_len -= 1
    return reserve_text

# 대칭수 저장 리스트
correct = []

# 3자리수 계산 이중 반복문
for i in range(999,100,-1) :
    for j in range(999,100,-1) :
        result = i * j

        # 대칭수 여부 확인
        if str(result) == reserse_txt(str(result)) :
            #print("correct = " ,  result)

            # 대칭수를 리스트에 등록
            correct.append(result)

# 대칭수 리스트 정렬
correct.sort()
# 대칭수 마지막 값 출력
print(correct[len(correct)-1])

# 906609




