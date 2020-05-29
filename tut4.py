#!/usr/bin/python
import os, time
x="Python Tutorial"
y=0
while y<=len(x):
	os.system("clear")
	print x[:y]
	time.sleep(0.1)
	y=y+1