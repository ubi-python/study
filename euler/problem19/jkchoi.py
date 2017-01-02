
years = range(1900, 2001)
months = [1,2,3,4,5,6,7,8,9,10,11,12]
days = [1,2,3,4,5,6,7]

def getDayCount(_year, _month):
    if ( _month in [4,6,9,11] ):
        return 30
    elif ( _month in [1,3,5,7,8,10,12]):
        return 31
    else:
        if ( 0 != _year % 4):
            return 28
        else:
            if ( _year not in [1600, 2000] ):
                return 29
            else:
                return 28

preFirst = 0
preDayCount = 0
mondayCount = 0
for y in years:
    for m in months:
        if ( 1900 == y and 1 == m):
            preFirst = 1
            preDayCount = getDayCount(y, m)
            mondayCount += 1
            continue

        first = preFirst + preDayCount%7
        if ( 7 < first):
            first -= 7

        #print(str(y) + " " + str(m) + " " + str(getDayCount(y,m)) +  " : " + str(first))
        if ( 1900 < y and 7 == first):
            print(str(y) + " " + str(m) + " " + str(getDayCount(y, m)) + " : " + str(first))
            mondayCount += 1

        preFirst = first
        preDayCount = getDayCount(y, m)

print(mondayCount)


