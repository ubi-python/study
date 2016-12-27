# 세 자연수 a, b, c 가 피타고라스 정리 a2 + b2 = c2 를 만족하면 피타고라스 수라고 부릅니다 (여기서 a < b < c ).
# 예를 들면 32 + 42 = 9 + 16 = 25 = 52이므로 3, 4, 5는 피타고라스 수입니다.
#
# a + b + c = 1000 인 피타고라스 수 a, b, c는 한 가지 뿐입니다. 이 때, a × b × c 는 얼마입니까?

import math

flag = False
for a in range(200, 1000):
    for b in range(1, 1000):
        print("b: "+str(b))
        if  a> b:
            continue
        for c in range(1, 1000):
            if b>c:
                continue
            if ( a+b+c == 1000 and c>b>a and (pow(a,2) + pow(b,2)) == pow(c,2)):
                print(a)
                print(b)
                print(c)
                print(a*b*c)
                flag = True
                break
        if flag :
            break
    print("a : " + str(a))
    if flag:
        break


print("end")