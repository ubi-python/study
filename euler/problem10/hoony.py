"""
10 이하의 소수를 모두 더하면 2 + 3 + 5 + 7 = 17 이 됩니다.

이백만(2,000,000) 이하 소수의 합은 얼마입니까?

"""
# 소수를 리스트에 누적하여 검증을 한다.

#최대 값
maxNum = 200*10000

#소수 저장 리스트
Prims = [2]

# 대상만큼 반복한다
for i in range(2,maxNum+1):

    # 소수여부 확인
    isPrime = True
    # 소수들로 나누어 확인한다.
    for j in Prims:

        #print("i,j,i%j --> ",i,j,i%j)
        if i%j == 0:
            isPrime = False
            break

    if isPrime :
        Prims.append(i)

    if i%10000 ==0:
        print("now checking --> ",i)

print(maxNum,"까지의 소수의 갯수 : ",len(Prims))

# 소수의 합
print(maxNum,"까지의 소수의 합 : ",sum(Prims))

# 2000000 까지의 소수의 갯수 :  148933
# 2000000 까지의 소수의 합 :  142913828922