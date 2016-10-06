# coding=utf-8
import collections

with open('mess.txt', 'r') as openfile:
    lines = openfile.readlines()

map = collections.OrderedDict()
for line in lines:
    for ch in line:
        if ch not in map:
            map[ch] = 1
        else:
            map[ch] += 1

result = ""
for key in map.keys():
    if (map[key] == 1):
        result += key

print(result)
