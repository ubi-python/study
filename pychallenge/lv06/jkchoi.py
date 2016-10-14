import zipfile

comment = ""
def print_info(archive_name):
    zf = zipfile.ZipFile(archive_name)
    for info in zf.infolist():
        print (info.filename)
        print ('\tComment:\t', info.comment)
        print ('\tSystem:\t\t', info.create_system, '(0 = Windows, 3 = Unix)')
        print ('\tZIP version:\t', info.create_version)
        print ('\tCompressed:\t', info.compress_size, 'bytes')
        print ('\tUncompressed:\t', info.file_size, 'bytes')
        print

def getContent(_no, zipFile):
    print("try : " + _no)
    filename = _no + ".txt"
    for info in zipFile.infolist():
        if ( filename == info.filename):
            return (info.comment, zipFile.read(filename).decode("UTF-8"))

zf = zipfile.ZipFile("channel.zip")


prefix = "Next nothing is "
no = "90052"
i = 1

comment = ""
while True :
    content = getContent(no, zf)
    comment += content[0].decode("UTF-8")
    text = content[1]
    print( str(i) + ". read : " + text)
    if prefix in text:
        no = text[text.find(prefix) + len(prefix):]
    else:
        break
    i += 1

print(comment)
# result : http://www.pythonchallenge.com/pc/def/hockey.html
# result : http://www.pythonchallenge.com/pc/def/oxygen.html