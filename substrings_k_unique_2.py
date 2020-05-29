# substrings_k_unique.py
def uniqueSubstring(s,k):
	res=[]
	i=0
	while i<=len(s)-k:
		temp=s[i:i+k]
		if len(set(temp))==len(temp):
			res.add(temp)
		i+=1
	return res
s = "awaglknagawunagwkwagl"
k = 4
res=uniqueSubstring(s,k)