
dic = {}


def proc(_n):
    if ( 0 == _n%2):
        return _n/2
    else:
       return  (3*_n) + 1

def count(_n):
    count = 0
    val = _n
    while (1 != val):
        val = proc(val)
        count += 1
        if ( str(val) in dic):
            count += dic[str(val)]
            dic[str(_n)] = count
            return count

    count += 1
    dic[str(_n)] = count
    return count


number = 0
result = 0
for i in range(1, 1000001):
    new = count(i)
    print(str(i) + " : " + str(new))
    if ( result < new):
        number = i
        result = new

print("result : " + str(number) + " : " + str(result) )