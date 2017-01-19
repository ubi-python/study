def permute(_result, _a, _l, _r):
    if ( _l == _r ):
        _result.append(_a)
    else:
        for i in range(_l, _r+1):
            b = _a[:]
            b.pop(_l)
            b.insert(_l, _a[i])
            b.pop(i)
            b.insert(i, _a[_l])
            permute(_result, b, _l + 1, _r)


base = ['0','1','2','3','4','5','6','7','8','9']
result = []
permute(result, base, 0, 9)
print(result[1000000-1])
print(result[1000000])

R = []
for _l in result:
    str = ""
    for s in range(0, len(_l)):
        str += _l[s]
    R.append(str)

list.sort(R)
print(R[1000000-1])
#2783915460