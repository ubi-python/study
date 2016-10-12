

def getContent(_no):
    print("try : " + _no)
    f = open("channel/" + _no + ".txt", 'r')
    data = ""
    while True:
        line = f.readline()
        if not line: break
        data += line
    f.close()
    return data


prefix = "Next nothing is "
no = "90052"
i = 1
total = 0
while True :
    total += int(no)
    text = getContent(no)
    print( str(i) + ". read : " + text)
    if prefix in text:
        no = text[text.find(prefix) + len(prefix):]
    else:
        break
    i += 1

print (total)
# result : http://www.pythonchallenge.com/pc/def/peak.html