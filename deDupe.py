# deDupe.py - Remove duplicates while maintainig order
def deDupe(items):
	seen=set()
	for item in items:
		if item not in seen:
			yield item
			seen.add(item)

def deDupeDict(items, key=None):
	seen=set()
	for item in items:
		val=item if key is None else key(item)
		if val not in seen:
			yield item
			seen.add(val)

def main():
	a=[12,14,54,12,98,54,31,7,-9,21,31]
	a_dict=[{'x':1,'y':2},{'x':1,'y':3},{'x':3,'y':2},{'x':1,'y':2}]
	print(list(deDupe(a)))
	print(list(deDupeDict(a)))
	print(list(deDupeDict(a_dict, key=lambda d:(d['x'],d['y']))))
	print(list(deDupeDict(a_dict, key=lambda d:(d['x']))))

if __name__ == '__main__':
	main()