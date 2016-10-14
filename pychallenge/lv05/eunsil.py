import pickle
import urllib.request

f = urllib.request.urlopen("http://www.pythonchallenge.com/pc/def/banner.p")
loadedContext = pickle.load( f)
print(loadedContext)

#urllib.request.urlretrieve("http://www.pythonchallenge.com/pc/def/banner.p", 'banner.p')
#f = open("banner.p", 'rb')
#loadedContext = pickle.load( f)
#print(loadedContext)

for i in loadedContext:
    #print((i))
    lineStr = ""
    for x in i: # i는 list,x는 tuple( [0],[1])
        lineStr= lineStr + str(x[0]*x[1])
    print(lineStr)
    #print ("".join([e[1] * e[0] for e in i]))