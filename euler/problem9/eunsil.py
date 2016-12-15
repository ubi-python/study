"""
9. 세 자연수 a, b, c 가 피타고라스 정리 a2 + b2 = c2 를 만족하면 피타고라스 수라고 부릅니다 (여기서 a < b < c ).
예를 들면 32 + 42 = 9 + 16 = 25 = 52이므로 3, 4, 5는 피타고라스 수입니다.

a + b + c = 1000 인 피타고라스 수 a, b, c는 한 가지 뿐입니다. 이 때, a × b × c 는 얼마입니까?
"""

#경우의 수 : a=1일때 b=2~ (1000-a)/2
# a=2 일때 .... a= a<b<c에 의해 1000/3 까지만 해도 됨.
import math

for a in range(1,int(1000/3)):
    for b in range(a+1, int((1000-a)/2)):
        leftValue = (a * a) + (b * b)
        tempC=math.sqrt(leftValue)
        if( tempC == int(tempC)  and (a+b+tempC)== 1000) :
            print(a*b*tempC)
            break


