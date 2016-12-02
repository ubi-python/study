"""
http://euler.synap.co.kr/prob_detail.php?id=16

215 = 32768 의 각 자리수를 더하면 3 + 2 + 7 + 6 + 8 = 26 입니다.

21000의 각 자리수를 모두 더하면 얼마입니까?
"""
def sum(num) :
    result = 0
    for i in str(num):
        result += int(i)
    return result

print("# 답 : ", sum(2**1000))

# 답 :  1366
