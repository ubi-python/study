max = 0

def checkPalindrome(i, j):
    inttoStr = str(i*j)
    if (len(inttoStr) % 2 != 0 ):
        return False
    halflen = int(len(inttoStr)/2)
    firstValue = inttoStr[0:halflen]
    secondvalue = inttoStr[:-(halflen+1):-1]
    if (firstValue == secondvalue):
       return True
    else:
        return False


for i in reversed(range(1000)):
    for j in reversed(range(1000)):
        if(checkPalindrome(i,j)):
            if(max < i*j):
               max = i*j

print(max)




