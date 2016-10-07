import urllib.request
import collections


def getContent(no):
    content = urllib.request.urlopen("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="+no).read()
    text = content.decode("utf-8")



print(getContent("12345"))