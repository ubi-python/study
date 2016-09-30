import string

base  =2
pow = 38
n = base
for i in range(1,pow) :
    n *=base

print(n)

# only small case
data = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

result = ""
for i in range(0, len(data)):
    c = ord(data[i])
    if 97 <= c <= 127:
        c +=2
        if ( c >  122 ):
            c -= (ord("z") - ord("a")+1)

    result += chr(c)


print("original : " + data)
print("result : " + result)

orimap = "abcdefghijklmnopqrstuvwxyz"
newmap = "cdefghijklmnopqrstuvwxyzab"
print(data.translate(str.maketrans(orimap,newmap)))
