input_str = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."


def convert_ch(ch):
    if not alphabet.isalpha():
        return ch

    ascii = ord(alphabet)
    if ascii >= 121:
        return chr(ascii + 2 - 26)
    else:
        return chr(ascii + 2)


answer = ''
for alphabet in input_str:
    answer += convert_ch(alphabet)

print(answer)

print('>>> another solution')

trans_table = str.maketrans('abcdefghijklmnopqrstuvwxyz', 'cdefghijklmnopqrstuvwxyzab')

print(input_str.translate(trans_table))
