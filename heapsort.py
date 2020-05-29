#heapsort.py
def heapify(a,i):
	l=2*i+1
	r=l+1
	if l<heap_size and a[l]>a[i]:
		largest=l
	else:
		largest=i 
	if r<heap_size and a[r]>a[largest]:
		largest=r 
	if largest!=i:
		a[i],a[largest]=a[largest],a[i]
		#print a
		heapify(a,largest)

def build_heap(a):
	print "Heap built. Array is as follows"
	for i in range(len(a)/2,-1,-1):
		#print i
		heapify(a,i)
	print a

def heapsort(a):
	print "Sorted. Array is as follows"
	global heap_size
	for i in range (len(a)-1,0,-1):
		a[0],a[i]=a[i],a[0]
		heap_size=heap_size-1
		heapify(a,0)
	print a

def parent(i):
	if i%2==1:
		return i/2
	else:
		return (i/2)-1

def insert_heap(a,x):
	print "Inserting",x,"into heap"
	global heap_size
	heap_size=heap_size+1
	i=heap_size-1
	a.append(0)
	while i>0 and a[parent(i)]<x:
		a[i]=a[parent(i)]
		i=parent(i)
	a[i]=x
	print a


a=[4,1,3,2,16,9,10,0,14,8,7,13,17]
print "Initial state of array"
print a
heap_size=len(a)
build_heap(a)
insert_heap(a,60);
insert_heap(a,121)
heapsort(a)
