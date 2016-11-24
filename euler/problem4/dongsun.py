maxPalindrome = 0
maxFirstNum = 0
maxSecondNum = 0

for firstNum in range(100, 999):
    for secondNum in range(100, 999):
        result = firstNum * secondNum
        # result가 대칭수인지 비교함
        if "".join(reversed(str(result))) == str(result):
            # result와 maxPalindrome 값 비교
            if maxPalindrome < result:
                maxFirstNum = firstNum
                maxSecondNum = secondNum
                maxPalindrome = result

print("maxFirstNum : " + str(firstNum))
print("maxSecondNum : " + str(secondNum))
print("maxPalindrome : " + str(maxPalindrome))
