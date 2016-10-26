

def getNext(_data):
    result = ""

    currentChr = _data[0]
    count = 1
    for i in range(1, len(_data)):
        if ( currentChr == _data[i]):
            count += 1
            continue
        else:
            result += str(count)
            result += currentChr
            currentChr = _data[i]
            count = 1
    result += str(count)
    result += currentChr
    return result

data  = "1"
print("0 : " + data)
for i in range(0,30):
    data = getNext(data)
    print(str(i+1) + " : " + data)

print("result : " + str(len(data)))

#5808