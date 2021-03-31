from functools import lru_cache
from tqdm import tqdm
import time, timeit

def fib(n: int):
    if n<=1:
        return 1
    else:
        return fib(n-1)+fib(n-2)

@lru_cache(maxsize=128)   
def fib_cached(n: int):
    if n<=1:
        return 1
    else:
        return fib_cached(n-1)+fib_cached(n-2)

def call_fib(n=40):
	for i in tqdm(range(n),ncols=100):
		fib(i)

def call_fib_cached(n=40):
	for i in tqdm(range(n),ncols=100):
		fib_cached(i)

def main():
	n=40
	cached_values, uncached_values=[],[]
	time_cached=timeit.timeit(call_fib_cached,number=1)
	print("Cached version: {:.3f} seconds\nOutput: %s".format(time_cached, ",".join(cached_values)))
	time_uncached=timeit.timeit(call_fib,number=1)
	print("Uncached version: {:.3f} seconds\nOutput: %s".format(time_uncached, ",".join(uncached_values)))


if __name__ == '__main__':
	main()
