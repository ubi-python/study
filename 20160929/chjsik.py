# encoding=utf-8

i = input("단수를 입력해주세요 : ")

for j in range(1,10):
    print(format("%s * %s = %d" % (i, j, j*int(i))))