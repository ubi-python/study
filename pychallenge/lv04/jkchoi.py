import urllib.request
import collections

baseurl = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="

def getContent(_no):
    print("try : " + _no)
    content = urllib.request.urlopen(baseurl + _no).read()
    return content.decode("utf-8")


prefix = "and the next nothing is "
no = "12345"
while True :
    text = getContent(no)
    print("response : " + text)
    if prefix in text:
        no = text[text.find(prefix) + len(prefix):]
    elif "Yes. Divide by two and keep going." in text:
        no = str( int(int(no) / 2)  )
    else:
        break

# result : http://www.pythonchallenge.com/pc/def/peak.html