import random
import copy
import time
import sys
def main():
	a=[]
	if sys.argv[1]=='1':
		print 'Testing with smaller arrays...'
		for x in range(10):
			a.append(random.randint(0,100))
		print a
		b=copy.deepcopy(a)
		start=time.time()
		mergeSort(a,0,len(a)-1)
		end=time.time()
		elapsed=end-start
		print 'Mergesort took ',elapsed,'seconds to execute'
		print a
		start=time.time()
		quickSort(b,0,len(b)-1)
		end=time.time()
		elapsed=end-start
		print 'Quicksort took ',elapsed,'seconds to execute'
		print b
	else:
		for x in range(100000):
			a.append(random.randint(0,1000000))
		b=copy.deepcopy(a)
		start=time.time()
		mergeSort(a,0,len(a)-1)
		end=time.time()
		elapsed=end-start
		print 'Mergesort took ',elapsed,'seconds to execute'
		start=time.time()
		quickSort(b,0,len(b)-1)
		end=time.time()
		elapsed=end-start
		print 'Quicksort took ',elapsed,'seconds to execute'

def mergeSort(a, start, end):
	if (start<end):
		mid=(start+end)/2
		mergeSort(a,start,mid)
		mergeSort(a,mid+1,end)
		merge(a, start, mid, end)

def merge(a,start,mid,end):
	left_len=mid-start+1
	right_len=end-mid
	left_temp=[0]*left_len
	right_temp=[0]*right_len
	for i in range(0,left_len):
		left_temp[i]=a[start+i]
	for i in range(0,right_len):
		right_temp[i]=a[mid+1+i]
	i=0
	j=0
	while i<left_len and j<right_len:
		if left_temp[i]<right_temp[j]:
			a[start]=left_temp[i]
			i=i+1
		else:
			a[start]=right_temp[j]
			j=j+1
		start=start+1
	while i<left_len:
		a[start]=left_temp[i]
		start=start+1
		i=i+1
	while j<right_len:
		a[start]=right_temp[j]
		start=start+1
		j=j+1


def quickSort(a, low, high):
	if low<high:
		pivotPoint=partition(a,low,high)
		quickSort(a,low,pivotPoint-1)
		quickSort(a,pivotPoint+1,high)

'''def partitionRandom(a,low,high):
	pivotPoint=random.randint(low,high)
	pivot=a[pivotPoint]
	i=low-1
	k=high+1
	for j in range(low,pivotPoint):
		if a[j]>pivot:
			k=
			a[j],a[pivotPoint]=a[pivotPoint],a[j]
	
	print low, high, pivotPoint		
	print a 
	return pivotPoint'''


def partition(a, low, high):
	#pivotPoint=random.randint(low,high)
	pivot=a[high]
	i=low-1
	k=high+1
	for j in range(low,high):
		if a[j]<=pivot:
			i=i+1
			a[i],a[j]=a[j],a[i]

	a[i+1],a[high]=a[high],a[i+1]
	return (i+1)



if __name__ == '__main__':
	main() 