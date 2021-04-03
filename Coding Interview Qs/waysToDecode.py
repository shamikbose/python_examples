#Ways to decode a message
from functools import lru_cache
from time import time
def encode(input_msg: str) -> str:
	output_msg=[]
	for c in input_msg.lower():
		output_msg.append(str(ord(c)-96))
	return "".join(output_msg)

@lru_cache(maxsize=64)
def decode(input_msg: str) -> int:
	if len(input_msg)==0:
		return 1
	if input_msg[0]=='0':
		return 0

	res=decode(input_msg[1:])
	if len(input_msg)>=2 and int(input_msg[:2]) <=26:
		res+=decode(input_msg[2:])
	return res

def decode_DP(input_msg: str, memo: list, max_len: int) -> int:
	if len(input_msg)==0:
		return 1
	if input_msg[0]=='0':
		return 0
	if memo[max_len-len(input_msg)]:
		return memo[max_len-len(input_msg)]
	res=decode_DP(input_msg[1:],memo,max_len)
	if len(input_msg)>=2 and int(input_msg[:2])<=26:
		res+=decode_DP(input_msg[2:],memo,max_len)
	memo[max_len-len(input_msg)]=res
	return res

msg="111111111111111111111111111111111111111111111"
memo=[None]*(len(msg)+1)
max_len=len(msg)
start=time()
res=decode(msg)
end=time()
print("Time with caching: {:.3f} seconds".format(end-start))
start=time()
res=decode_DP(msg,memo, len(msg))
end=time()
print("Time without caching: {:.3f} seconds".format(end-start))