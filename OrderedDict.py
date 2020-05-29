#OrderedDict.py
from collections import OrderedDict

d=OrderedDict()
d['a']=65
d['c']=66
d['b']=67
d['d']=68
print("Ordered Dictionary")
for key in d:
	print(key,d[key])

d={}
d['a']=65
d['c']=66
d['b']=67
d['d']=68
print("Regular Dictionary")
for key in d:
	print(key,d[key])
