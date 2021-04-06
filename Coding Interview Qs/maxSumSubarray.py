# Given an array containing positive and negative integers,
# find the subarray with the largest sum
import random, time


def createArray(size: int, min_range: int = -100, max_range: int = 100) -> list:
    res = [random.randint(min_range, max_range) for _ in range(size)]
    return res


def maxSumSubarrayNaive(nums):
    max_sum = -float("inf")
    max_i, max_j = 0, 0
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            temp_sum = sum(nums[i:j])
            if temp_sum > max_sum:
                max_i, max_j = i, j
                max_sum = temp_sum
    return max_sum, max_i, max_j


def maxSumSubarrayKadane(nums):
    max_so_far = -float("inf")
    max_ending_here = 0
    for i in nums:
        max_ending_here += i
        if max_so_far < max_ending_here:
            max_so_far = max_ending_here
        if max_ending_here < 0:
            max_ending_here = 0
    return max_so_far


def helper(nums, lo, hi, mid):
    sm = 0
    left_sum = -float("inf")
    for i in range(mid, lo - 1, -1):
        sm += nums[i]
        if sm > left_sum:
            left_sum = sm

    sm = 0
    right_sum = -float("inf")
    for i in range(mid + 1, hi + 1):
        sm += nums[i]
        if sm > right_sum:
            right_sum = sm

    return max(left_sum + right_sum, left_sum, right_sum)


def maxSumSubarrayDP(nums, lo, hi):
    if lo == hi:
        return nums[lo]

    mid = (lo + hi) // 2
    return max(
        maxSumSubarrayDP(nums, lo, mid),
        maxSumSubarrayDP(nums, mid + 1, hi),
        helper(nums, lo, hi, mid),
    )


size = 5000
min_range = -300
max_range = -1 * min_range
nums = createArray(size, min_range, max_range)
print("Array created\nSize: {}\nRange {} to {}".format(size, min_range, max_range))

print("Naive method")
start = time.time()
res_1, i, j = maxSumSubarrayNaive(nums)
end = time.time()
print("Result: {}\nTime taken:{} seconds".format(res_1, end - start))
print("Divide and Conquer method")
start = time.time()
res_2 = maxSumSubarrayDP(nums, 0, len(nums) - 1)
end = time.time()
print("Result: {}\nTime taken:{} seconds".format(res_2, end - start))
print("Kadane method")
start = time.time()
res_3 = maxSumSubarrayKadane(nums)
end = time.time()
print("Result:{}\nTime taken:{} seconds".format(res_3, end - start))
