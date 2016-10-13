import os
import sys
from getInternetText import getText


root = os.path.dirname(__file__)
sys.path.append(root )
print(root)


targetText = getText()
print(targetText)
cha = {}
