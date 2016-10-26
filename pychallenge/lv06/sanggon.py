import collections
import re
from zipfile import *


def find_nothing_from_value(val):
    # print(val)
    match = re.compile(r"Next nothing is (\d+)").search(val)
    if match:
        return match.group(1)
    else:
        return None


answer = ''
q_dic = collections.OrderedDict()
try:
    with ZipFile('channel.zip', 'r') as channelZip:
        file_name_list = channelZip.namelist()
        for filename in file_name_list:
            file_content = channelZip.read(filename)
            q_dic[filename] = file_content.decode("utf-8")
except BadZipfile:
    print('Bad Zip file')

condition = '90052'

zip = ZipFile('channel.zip', 'r')

while True:
    if not condition:
        break
    print(zip.getinfo(condition + '.txt').comment.decode("utf-8"), end='')
    condition = find_nothing_from_value(q_dic[condition + '.txt'])

zip.close()


# result = Collect the comments.
