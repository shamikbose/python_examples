from functools import lru_cache
from tqdm import tqdm
import time

def fib(n: int):
    if n<=1:
        return 1
    else:
        return fib(n-1)+fib(n-2)

@lru_cache(maxsize=None)   
def fib_cached(n: int):
    if n<=1:
        return 1
    else:
        return fib_cached(n-1)+fib_cached(n-2)

def main():
	n=40

	start_time=time.time()
	for i in tqdm(range(1,n), ncols=80):
	    fib_cached(i)
	end_time=time.time()
	print('Cached version took {:.4f} seconds'.format(end_time-start_time))
	print(fib_cached.cache_info())

	start_time=time.time()
	for i in tqdm(range(1,n), ncols=80):
	    fib(i)
	end_time=time.time()
	print('Uncached version took {:.4f} seconds'.format(end_time-start_time))

if __name__ == '__main__':
	main()
