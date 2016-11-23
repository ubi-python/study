
def isPalindrome(n):
    nstr = str(n)

    if ( 0 != len(nstr) % 2 ):
        return False

    for i in range(0, int(len(nstr) / 2) ):
        if ( nstr[i] != nstr[len(nstr) - i - 1] ):
            return False

    return True

result = 0
for i in range(100, 999):
    for j in range(100, 999):
        n = i * j

        if (isPalindrome(n) ):
            if ( n > result):
                result = n


print(result)