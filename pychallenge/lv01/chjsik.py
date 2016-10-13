# coding=utf-8

initText = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj"

inTab = "abcdefghijklmnopqrstuvwxyz"
outTab = "cdefghijklmnopqrstuvwxyzab"

transTab = str.maketrans(inTab, outTab)

print(initText.translate(transTab))

print("result : "+"map".translate(transTab))


