# everybody thinks twice before solving this
# 1
text = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.".upper()
clone = ""

alpabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

flag = 1
index = 0
while(flag) :
    x = 0

    #if( text[index] == " " ):
    #    print("111111111111111111111")
    #    clone = clone + " "
    #elif(text[index]=="."):
    #    clone = clone + "."
   # elif (text[index] == "'"):
    #    clone = clone + "'"
    if text[index] not in alpabet:
        clone = clone + text[index]
    else:
        while(1):
            if( text[index] == alpabet[x]):
                if( x+2 > len(alpabet)-1):
                    clone = clone + alpabet[x+2 -len(alpabet)]
                    break
                else:
                    clone = clone+ alpabet[x+2]
                    break
            x = x+1

   # if( text[index] == 'K'   ):
    #    clone=clone[:index] + "M" + clone[index+1:]
     #   print('---M')
   # elif (text[index] == 'O' ):
#        clone = clone[:index] + "Q" + clone[index+1:]
#        print('---Q')
#    elif (text[index] == 'E' ):
#        clone = clone[:index] + "G" + clone[index+1:]
#        print('---G')

    if( index+1 >= len(text)):
        flag = 0
    print(clone)
    index= index+1




