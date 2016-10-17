import urllib.request
import collections

req = urllib.request.Request('http://www.pythonchallenge.com/pc/def/ocr.html')
with urllib.request.urlopen(req) as response:
   the_page = response.read()
   str = the_page.decode("utf-8")
   str = str.split("<!--")[2].split("-->")[0]
   map = collections.OrderedDict()

   for ch in str:
      if ch not in map:
         map[ch] = 1
      else:
         map[ch] += 1

   result = ""
   for key in map.keys():
      if map[key] == 1:
         result += key

   print(result)






