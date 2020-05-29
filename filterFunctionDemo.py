# filterFunctionDemo.py
mylist=[5,8,13,-4,5,7,31,-12,0,1,-1]
print([n for n in mylist if n>0])
print([n for n in mylist if n<=0])
gen=(n for n in mylist if n<=0)
for x in gen:
	print (x,end=" ")
print()
mylist_2=[5,8,13,-4,5,'8x',7,31,-12,0,1,-1,'A','-']
def isPositiveInt(val):
	try:
		x=int(val)
		if x>0:
			return True
		else:
			return False
	except ValueError:
		return False

ivals=list(filter(isPositiveInt,mylist_2))
print (ivals)