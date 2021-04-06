from time import time
from functools import lru_cache

# @lru_cache(maxsize=16)
def climbStairs(n: int) -> int:
    if n == 1:
        return 1
    if n == 2:
        return 2
    else:
        return climbStairs(n - 1) + climbStairs(n - 2)


def climbStairsDP(n: int, memo: list) -> int:
    if memo[n]:
        return memo[n]
    else:
        memo[n] = climbStairsDP(n - 1, memo) + climbStairsDP(n - 2, memo)
        return memo[n]


def climbStairsSteps(n: int, steps):
    if n == 0:
        return 1
    total = 0
    for i in steps:
        if n - i >= 0:
            total += climbStairsSteps(n - i, steps)
    return total


n_steps = 10
memo = [None] * (n_steps + 1)
memo[0], memo[1] = 1, 1
steps = [1, 3, 5]
start = time()
print(climbStairs(n_steps))
end = time()
print("Time taken with recursion: {:.3f} seconds".format(end - start))
start = time()
print(climbStairsDP(n_steps, memo))
end = time()
print("Time taken with DP: {:.3f} seconds".format(end - start))
start = time()
print(climbStairsSteps(n_steps, steps))
end = time()
print("Time taken with specified step sizes: {:.3f} seconds".format(end - start))
