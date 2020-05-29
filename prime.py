#!/usr/bin/python
def prime(z):
	result=[]
	for n in range(2,z):
		for x in range(2,n/2):
			if n%x==0:
				#print n,' is non-prime'
				break
		else:
			result.append(n)
	return result
x= prime(100)
print x