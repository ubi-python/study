# level = input("몇단을 원하세요?")

while (1):
    inputNum = int(input("구구단 중 원하시는 단의 숫자를 입력하세요 : "))

    if inputNum == 99:
        break

    for a in range(1, 10):
        print("{}".format(inputNum * a))
