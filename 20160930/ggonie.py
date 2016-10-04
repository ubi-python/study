answer = pow(2, 38)
print(answer)

if 2 ** 38 == answer:
    print('good job!')

question = '''
g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.
'''

print(question)

answer = ''
for alphabet in question:
    if alphabet.isalpha():
        # as
        ascii = ord(alphabet)
        answer += chr(ascii + 2)
    answer += alphabet

print(answer)


# print("orgin : ", question)
# question = question.replace('k', 'm')
# print("first convert : ", question)
# question = question.replace('o', 'q')
# question = question.replace('e', 'g')
