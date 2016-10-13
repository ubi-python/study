import urllib.request
import collections
import pickle


content = urllib.request.urlopen("http://www.pythonchallenge.com/pc/def/banner.p").read()

#print(content)
#print(type(content))

ex = pickle.loads(content)
print(ex)
print(type(ex))

for string in ex:
#    print(string)
#    print(type(string))
    val = ""
    for innerString in string:
#        print(innerString)
#        print(type(innerString))

        for i in range(0, innerString[1]):
            val += innerString[0]
    print(val)


# channel