'''
앞에서부터 읽을 때나 뒤에서부터 읽을 때나 모양이 같은 수를 대칭수(palindrome)라고 부릅니다.
두 자리 수를 곱해 만들 수 있는 대칭수 중 가장 큰 수는 9009 (= 91 × 99) 입니다.
세 자리 수를 곱해 만들 수 있는 가장 큰 대칭수는 얼마입니까?
대칭수 전체를 찾는다?
100*100
100000 <= x
1000000 > x
'''


# import datetime


def is_palindrome(check_num):
    s_num = str(check_num)
    if len(s_num) != 6:
        return False
    top = s_num[0:3]
    bottom = s_num[3:6]
    bottom = bottom[::-1]
    if top == bottom:
        return True


def is_palindrome2(check_num):
    s_num = str(check_num)
    if len(s_num) != 4:
        return False
    top = s_num[0:2]
    bottom = s_num[2:4]
    bottom = bottom[::-1]
    if top == bottom:
        return True


chk = True
for fnum in range(999, 100, -1):
    print('=========={}==========='.format(fnum))
    for snum in range(999, 100, -1):
        palindrome = fnum * snum
        chk = is_palindrome(palindrome)
        if chk:
            print('{} * {} = {}'.format(fnum, snum, palindrome))
            break
    if chk:
        break



# 인수분해??
