def pairSum(nums, target):
    hashDict = {}
    target -= 30
    if not nums:
        return None
    for i in range(len(nums)):
        if nums[i] in hashDict:
            return hashDict
