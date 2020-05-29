def pairSumHash(a, sum):
	hash_dict={}
	count=0
	for i in a:
		hash_dict[i]=sum-i
	all_keys=hash_dict.keys()
	all_vals=hash_dict.values()
	for val in all_vals:
		if val in all_keys:
			count=count+1
			print val,hash_dict[val]
	if(count==0):
		print "No combination found"

a=[95,13,88,100,23,28]
pairSumHash(a,123)

		