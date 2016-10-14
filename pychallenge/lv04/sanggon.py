import urllib3

# import re

http_pool = urllib3.PoolManager()

divide = False


def request_url_for_nothing(nothing, count):
    # if divide == True:
    # nothing = int(nothing)/2
    r = http_pool.request('GET', 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={}'.format(nothing))
    print('{1}:{0}'.format(r.data, count))
    res = r.data.decode("utf-8")

    if res == 'Yes. Divide by two and keep going.':
        print('yes!!!!!!!!!!!!!!!!!!!!!!!!!!!1')
        nothing = int(nothing) / 2
        r = http_pool.request('GET', 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={}'.format(nothing))
        res = r.data.decode("utf-8")
    word_list = res.split(' ')
    # print(word_list)

    if word_list[len(word_list) - 1].isalpha():
        print("answer :   {0}".format(word_list))

    last_pos = len(word_list) - 1
    return word_list[last_pos]
    # result = re.search('\d+$', res)
    # print(result)
    # return result.group(0)


param = '16044'
for cnt in range(399):
    if param.isalpha():
        break
    param = request_url_for_nothing(param, cnt)
print(param)

# Yes. Divide by two and keep going.
