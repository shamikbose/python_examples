## Given a shifted sorted array, find an element in it

## Naive approach:
## Ignore that the array is sorted and shifted and treat
## it as an unsorted array. Linear search O(log n)

# Better approach:
# Find the point where it's shifted and run two binary searches


import random

def find_pivot(arr: list) -> int:
	'''
	Given a rotated array, finds the pivot point
	'''
	#not rotated
	if arr[0]<arr[-1]:
		return 0
	lo,hi=0, len(arr)-1
	while lo<=hi:
		mid=(lo+hi)//2
		#Check if mid+1 is pivot
		if mid<len(arr)-1 and arr[mid]>arr[mid+1]:
			return mid+1
		#Check in upper part of array
		elif arr[lo]<=arr[mid]:
			lo=mid+1
		#Check in lower part of array
		else:
			hi=mid-1
	return 0

def binary_search(arr: list, key: int) -> int:
	'''
	Given a list and a key, the algorithm returns a position 
	if the element is found, else returns -1
	'''
	if len(arr)==1:
		if arr[0]==key:
			return 0
		else:
			return -1
	lo, hi=0, len(arr)-1
	while lo<=hi:
		mid=(lo+hi)//2
		if arr[mid]==key:
			return mid
		elif arr[mid]>key:
			hi=mid-1
		else:
			lo=mid+1
	return -1


def test_code():
	'''
	Testing code to check the pivot point is computed correctly
	'''
	arr_size=100
	k=random.randint(1,arr_size)
	arr=[random.randint(0,500) for _ in range(arr_size)]
	key=random.choice(arr)
	arr.sort()
	arr=arr[k:]+arr[:k]
	res=find_pivot(arr)
	key_pos=-1
	if arr[res]==key:
		key_pos=res
	else:
		res_1=binary_search(arr[:res], key)
		res_2=binary_search(arr[res:], key)+res
		key_pos=max(res_1, res_2-res)
		if key_pos==res_2-res:
			key_pos+=res
	output="Found at position {}".format(key_pos) if key_pos!=-1 else "Not found"
	print(arr, "Pivot at {}".format(res), "\n", "Key:{}".format(key), output)

def main():
	test_code()
	

if __name__ == '__main__':
	main()

