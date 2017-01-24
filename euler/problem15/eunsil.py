"""
15. 아래와 같은 2 × 2 격자의 왼쪽 위 모서리에서 출발하여 오른쪽 아래 모서리까지 도달하는 길은 모두 6가지가 있습니다 (거슬러 가지는 않기로 합니다).


그러면 20 × 20 격자에는 모두 몇 개의 경로가 있습니까?
"""
def increase(startRow, startCol, maxCount, count):
    rowCount = 0
    if( startRow < maxCount):
        rowCount=increase( startRow+1, startCol, maxCount, count)
    else:
        rowCount += 1
    colCount=0
    if (startCol < maxCount):
        colCount = increase(startRow , startCol+1, maxCount, count)
    else:
        colCount += 1
    return rowCount+colCount





def getRouteCount( row, col):
    count = 0
    count2 = 0

    return increase( 0,0 ,row,0)

print( getRouteCount( 2,2))