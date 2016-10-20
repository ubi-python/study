# banner.p 가져오기
# import re
import pickle
from pathlib import Path

import urllib3


def retrieve_banner_p():
    http_pool = urllib3.PoolManager()
    r = http_pool.request('GET', 'http://www.pythonchallenge.com/pc/def/banner.p')
    return r.data
    # return str(restr)


banner_p = retrieve_banner_p()
my_file = Path('banner.p')
if not my_file:
    wfile = open('banner.p', 'wb')
    wfile.write(banner_p)
    wfile.close()

results = pickle.load(open('banner.p', 'rb'))

# print(results)

for point_list in results:
    print(point_list)

print('\n\n')

line = 0
for point_list in results:
    # print(line, end="")
    # line += 1
    for points in point_list:
        print('{}'.format(points[0] * int(points[1])), end="")
    print('')
