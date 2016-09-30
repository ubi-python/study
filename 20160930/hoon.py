# 주어진 문장
txt = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
# 문장 길이
cnt = len(txt)
# 변환 후 문자열
result = ""
# 치환 전 문자열
src = ""

# 문장 길이 만큼 반복
for idx in range(0, cnt):

    # 한 글자 씩 가져옴
    a = txt[idx]

    src = src + a

    # ascii 값 조회
    i = ord(a)

    # 만일 a~z까지 값이면 다음 두번째 문자로 치환
    # a = 97 , z = 122
    if 97 <= i <= 122:
        i = i + 2

        # (단 z를 넘어가면 다시 a 부터 시작)
        if i > 122:
            i -= 26
        result += chr(i)
        print(src)
        print(result)

    # 그렇지 않으면 현재 문자 그대로 사용
    else:
        result = result + a
        print(src)
        print(result)

    print('치환 : {0} -> {1}'.format(a, chr(i)))

print(result)
# 결과 : i hope you didnt translate it by hand. thats what computers are for. doing it in by hand is inefficient and that's why this text is so long. using string.maketrans() is recommended. now apply on the url.

