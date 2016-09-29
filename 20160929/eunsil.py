#encoding(utf-8)
number = input("몇단? :")

secondNum = [1,2,3,4,5,6,7,8,9]
for i in secondNum:
     print (int(number) *i)

for x in secondNum:
    for y in secondNum:
        print( "{:d} * {:d} = {}".format( x, y , x*y))