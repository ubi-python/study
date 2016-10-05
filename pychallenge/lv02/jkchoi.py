import urllib.request
import collections

content = urllib.request.urlopen("http://www.pythonchallenge.com/pc/def/ocr.html").read()

#print(content)
#print(type(content))

text = content.decode("utf-8")
#print(text)


ex = text[text.find("<!--", text.find("<!--")+1) + 5 : text.rfind("-->") - len(text)]
#print (ex)


dict = collections.OrderedDict()
for i in range(0, len(ex)):
    c = ex[i]
    if ( c in dict.keys() ):
        dict[c] = dict[c] + 1
    else:
        dict[c] = 1

#print (dict)

result = ""
for key in dict.keys():
    if ( 1 == dict[key]):
        result += key

print (result)

