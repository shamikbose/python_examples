#!/usr/bin/python
from __future__ import print_function
from math import log, floor
if __name__=="__main__":
	y=int(input("Input a number > 1:"))
	x=y
	count=0
	while x > 0:
		x=x//2
		count+=1
	print("Approximate log_2 value of "+str(y) +" is "+str(count -1))
	assert abs(floor(log(y,2))-count+1) < 0.01, \
		"Calculation error"
