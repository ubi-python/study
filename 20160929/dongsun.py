# coding=utf-8

# 구구단 출력
# for i in range(2, 10):
#    for j in range(1, 10):
#        print(str(i) + "*" + str(j) + " = " + str(i * j))


# 입력 구구단
val = int(input("출력할 구구단을 입력하세요:"))

for x in range(1, 10):
    print("{} * {} = {}".format(val, x, val * x))
