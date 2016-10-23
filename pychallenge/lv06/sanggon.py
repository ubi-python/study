import collections
import re
from zipfile import *

findnothing = re.compile(r"nothing is (\d+)").search
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

for k, v in q_dic.items():
    print('{0} : {1}'.format(k, v))
    if condition in k:
        match = findnothing(v)
        if match:
            condition = match.group(1)
            print('next condition is {}'.format(condition))
    elif condition in v:
        match = re.compile(r"(\d+).txt").search(k)
        if match:
            condition = match.group(1)
            print('next condition is {}'.format(condition))
    else:
        continue
