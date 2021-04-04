# Given login and logout times of users (in ints, e.g. [2, 10], [5, 8]) 
# find the peak load interval
import random

def create_intervals(min_time: int, max_time: int, user_count:int):
	'''
	This will create a list of intervals of size user_count
	Each interval will be monotonically increasing
	'''
	intervals=[]
	for i in range(user_count):
		start=random.randint(min_time, max_time-1)
		end=random.randint(start+1, max_time)
		intervals.append([start,end])
	return intervals

def maxLoad(intervals):
	'''
	The idea here is to sort the login and logout times of all the users
	Then we merge them and keep track of logouts and lgogins
	'''
	print(intervals)
	logins=[x[0] for x in intervals]
	logouts=[x[1] for x in intervals]
	logins.sort()
	logouts.sort()
	users=0
	max_users=0
	time_in=logins[0]
	time_out=logouts[0]
	i,j=0,0
	while i<len(intervals) and j<len(intervals):
		if logins[i]<=logouts[j]:
			users+=1
			print("T-{:4d}:New user in system. User count:{}".format(logins[i],users))
			if users>max_users:
				max_users=users
				time_in=logins[i]
				time_out=logouts[j] if j<len(intervals)-1 else 1440
				print("New peak load: {}".format(max_users))
			i+=1
		else:
			users-=1
			print("T-{:4d}: User logged out. User count: {}".format(logouts[j],users))
			j+=1
	
	for lo_times in logouts[j:]:
		users-=1
		print("T-{:4d}: User logged out. User count: {}".format(lo_times,users))
	return time_in, time_out, max_users




min_time, max_time=0,1440
user_count=5
intervals = create_intervals(min_time,max_time,user_count)
res=maxLoad(intervals)
print("Max load of {} was between T-{:4d} and T-{:4d}".format(res[2],res[0],res[1]))