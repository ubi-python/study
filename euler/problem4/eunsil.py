"""
앞에서부터 읽을 때나 뒤에서부터 읽을 때나 모양이 같은 수를 대칭수(palindrome)라고 부릅니다.

두 자리 수를 곱해 만들 수 있는 대칭수 중 가장 큰 수는 9009 (= 91 × 99) 입니다.

세 자리 수를 곱해 만들 수 있는 가장 큰 대칭수는 얼마입니까?
"""

frist  = 999
second = 999

def bothDiscount(a,b):
    while(True):
        #print( "a:" +str(a) + " b:" +str(b))
        m= str(a * b)
        print(m)
        prev=m[:int(len(m)/2)]
        tail = m[round(len(m)/2 +0.1):]
        isPalindrome = True
        for i in range(0, len(prev)):
            if ( prev[i:i+1 ] != tail[ len(tail)-i-1: len(tail)-i]):
                isPalindrome=False
                break
        if( isPalindrome):
            return [a,b,m]
        else:
            a= a-1
            b=b-1

def oneDiscount(a,b):
    list = []
    while (True):
       # print("a:" + str(a) + " b:" + str(b))
        m = str(a * b)
        #print(m)
        prev = m[:int(len(m) / 2)]
        tail = m[round(len(m) / 2 + 0.1):]
        isPalindrome = True
        for i in range(0, len(prev)):
            if (prev[i:i + 1] != tail[len(tail) - i - 1: len(tail) - i]):
                isPalindrome = False
                break
        if (isPalindrome):
            list.append(([a, b,m]))
            a = a - 1
        elif( a==100):
            if(b==100):
                return list
            b= b-1
            a= b
        else:
            a = a - 1

#print(bothDiscount(frist, second))
result=(oneDiscount(frist,second))
print(result   )
num1=0
num2=0
maxNum = 0
for i in result:
    if( maxNum < int(i[2]) ):
        maxNum = int(i[2])
        num1 = int(i[0])
        num2 = int(i[1])

print( str( num1) +"// "+str( num2)+"// "+str( maxNum))



