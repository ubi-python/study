"""
http://euler.synap.co.kr/prob_detail.php?id=9
세 자연수 a, b, c 가 피타고라스 정리 a2 + b2 = c2 를 만족하면 피타고라스 수라고 부릅니다 (여기서 a < b < c ).
예를 들면 32 + 42 = 9 + 16 = 25 = 52이므로 3, 4, 5는 피타고라스 수입니다.

a + b + c = 1000  인 피타고라스 수 a, b, c는 한 가지 뿐입니다. 이 때, a × b × c 는 얼마입니까?

"""


# 피카고라스 수 체크
def isPyTha(num1, num2, num3):
    if(num3**2 ==(num1**2 + num2**2)):
        return True
    else:
        return False

# 결과값
result = 0

for i in range(1,1001):
    for j in range(i+1,1001-i):
        for k in range(j+1,1001-(i+j)):

            #print("check : ", i,j,k)
            if(isPyTha(i,j,k)==True):

                print("피타고라스 수 : ",i,j,k)
                if(i+j+k == 1000):
                    result = i*j*k
                    break

        if result > 0 : break

        if(i+j+k)>1000 :
            print("합이 1000 over --> break")
            break

    if result > 0 : break

print("답 : ", result)

# 피타고라스 수 :  200 375 425
# 답 :  31875000