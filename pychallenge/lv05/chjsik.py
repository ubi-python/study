# coding=utf-8
import urllib.request
import pickle

requestUrl = "http://www.pythonchallenge.com/pc/def/peak.html/banner.p";

data = urllib.request.urlopen(requestUrl).read()

print(type(data))

print(data)


