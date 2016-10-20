from PIL import Image
im = Image.open("oxygen.png")
pix = im.load()
print(pix)
print(type(pix))

width, height = im.size

print(width)
print(height)

p = pix[0,0]

print(p)
print(type(p))


data = ""
#for i in range(0, height):
for i in range(int(height/2), int(height/2) + 1):
    for j in range(0, width, 7):
#        print("{}, {} : ".format(j, i) + str(pix[j,i][0]))
        data += chr(pix[j,i][0])

print(data)


#[105, 110, 116, 101, 103, 114, 105, 116, 121]
array = [105, 110, 116, 101, 103, 114, 105, 116, 121]
result = ""
for i in range(0, len(array)):
    result +=chr(array[i])
print(result)