import inflect


def func(_w):
    count = 0
    for i in range(0, len(_w)):
        if  (' ' == _w[i] or '-' == _w[i] ) :
            continue
        count += 1
    return count


p = inflect.engine()

total_count = 0
for i in range(1,1001):
    w = p.number_to_words(i)
    total_count += func(w)


print(total_count)
