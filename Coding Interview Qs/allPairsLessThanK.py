# Given a list of numbers and K, return the number of pairs 
# where the sum of the pair is less than K
from collections import defaultdict
import random, time
list_size=1000
max_range=1000
nums=[random.randint(1,max_range) for i in range(list_size)]

def bruteForceSolution(nums: list, k:int)-> list:
	res=[]
	count=0
	for idx_1,num_1 in enumerate(nums):
		for idx_2, num_2 in enumerate(nums[idx_1+1:]):
			if num_1+num_2<k:
				res.append((num_1,num_2))
				count+=1
	return res, count

def sortedSolution(nums: list, k: int)-> list:
	res=[]
	count=0
	nums.sort()
	front,back=0,len(nums)-1
	while(front<back):
		if (nums[front]+nums[back])<k:
			temp=[(nums[front], nums[j]) for  j in range(front+1,back+1)]
			res.extend(temp)
			count+=(back-front)
			front+=1
		else:
			back-=1
	return res, count
	
k=2000
start=time.time()
res_1,count=bruteForceSolution(nums,k)
end=time.time()
print("Brute Force Solution:\n{}... {} pairs\nTime taken: {:.3f} seconds".format(res_1[:5],count,end-start))
start=time.time()
res_2,count=sortedSolution(nums,k)
end=time.time()
print("Sorted Solution:\n{}... {} pairs\nTime taken: {:.3f} seconds".format(res_2[:5],count, end-start))