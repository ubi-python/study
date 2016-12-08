"""
1부터 5까지의 숫자를 영어로 쓰면 one, two, three, four, five 이고,
각 단어의 길이를 더하면 3 + 3 + 5 + 4 + 4 = 19 이므로 사용된 글자는 모두 19개입니다.

1부터 1,000까지 영어로 썼을 때는 모두 몇 개의 글자를 사용해야 할까요?

참고: 빈 칸이나 하이픈('-')은 셈에서 제외하며, 단어 사이의 and 는 셈에 넣습니다.
   예를 들어 342를 영어로 쓰면 three hundred and forty-two 가 되어서 23 글자,
   115 = one hundred and fifteen 의 경우에는 20 글자가 됩니다.

"""

# 딕셔너리
# 1의자리
pos_one = {1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six", 7:"seven", 8:"eight", 9:"nine"}
# 10자리수
teen_pos = {0:"ten", 1:"eleven", 2:"twelve", 3:"thirteen", 4:"fourteen", 5:"fifteen", 6:"sixteen", 7:"seventeen", 8:"eighteen", 9:"nineteen"}
# 10단위
ten_pos = {1:"ten", 2:"twenty", 3:"thirty", 4:"forty", 5:"fifty", 6:"sixty", 7:"seventy", 8:"eighty", 9:"ninety"}



def char_cnt(number):

    result = ""

    num = str(number)
    position = len(num) # 길이

    is_teen = False
    is_hundred = False
    for i in num:

        if position == 4 and int(i) > 0: #천단위
            result += pos_one[int(i)]
            result += " thousand  "

        elif position == 3 and int(i) > 0: #백단위
            result += pos_one[int(i)]
            result += " hundred "
            if number % 100 > 0 :
                result += "and "

        elif position == 2 and int(i) > 1: #십단위

            result += ten_pos[int(i)]
            result += " "

        elif position == 2 and int(i) == 1: #1십단위

            is_teen = True
            position -= 1
            continue

        elif position == 1: #일단위

            if int(i) == 0 :
                if is_teen == True:
                    result += teen_pos[int(i)]

            elif int(i) > 0 :
                if is_teen == True:
                    result += teen_pos[int(i)]
                else:
                    result += pos_one[int(i)]

        position -= 1

    return result

# print(char_cnt(1111))
#print(char_cnt(1111).replace(" ", ""))
#print(len(char_cnt(1111).replace(" ", "")))

len_sum = 0

for num in range(1,1001):

    text = char_cnt(num)
    print(num, text, len(text.replace(" ", "")))

    len_sum += len(text.replace(" ", ""))

print("# 답 : %d" % len_sum)

# 답 : 21124


# ---------------------------------------------
from num2words import num2words

ans = 0
for i in range(1,1001):
    a = num2words(i)
    a = a.replace("-","")
    a = a.replace(" ","")
    ans = ans + len(a)
print("# 다른 사람 코딩 결과 : ", ans)
