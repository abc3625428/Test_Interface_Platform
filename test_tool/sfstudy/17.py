

def twoSum(nums, target):

    for i in nums[::-1]:
        if i >= target:
           nums.remove(i)

    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i] + nums [j] == target :
                return i,j
    return []




print(twoSum([2,7,11,15],9))