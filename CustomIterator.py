# CustomIterator.py
def customrange(start,stop,increment):
	x=start
	while x<stop:
		yield x
		if x%2==0:
			x+=increment*3
		else:
			x-=increment

for n in customrange(2,16,1):
	print (n)