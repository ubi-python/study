import urllib.request
import zipfile
import re

#response = urllib.request.urlopen('http://www.pythonchallenge.com/pc/def/channel.zip')
urllib.request.urlretrieve('http://www.pythonchallenge.com/pc/def/channel.zip', 'channel2.zip')

file = zipfile.ZipFile('channel2.zip',"r")
nameList=file.namelist()
infoList =file.infolist()
readmeFile=file.read("readme.txt")
print(file.getinfo("readme.txt"))
#print(readmeFile)

comments=[]
fileNameNum = "90052"
while(1):
    try:
        fileContext=( file.read(fileNameNum + ".txt").decode(encoding='UTF-8'))
        a = re.findall("[0-9]{1,5}", str(fileContext))
        indexOfText = len(a) - 1
        comments.append((file.getinfo(fileNameNum + ".txt" ).comment.decode(encoding='UTF-8')))

        fileNameNum=str(a[indexOfText])
        print(fileNameNum)
    except Exception:
        print(fileContext)
        break

print("".join((comments)))
#---- nama List ----#
"""
for info in nameList:
    print(info)
    if( info == "readme.txt"):
        continue
    number=re.search("[0-9]{1,5}",info)
    print(number.group(0))
    #if(info =="readme.txt"):
    print(file.read(info))
"""

"""
for info in infoList:
    print(info)
    if(info.filename =="readme.txt"):
        print("dddd")
"""

#with zipfile.ZipFile('channel2.zip','w') as myzip:
#    myzip.write('eggs.txt')
