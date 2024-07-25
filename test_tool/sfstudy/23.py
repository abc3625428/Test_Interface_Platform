
def removeDuplicates(nums):

    n = len(nums)

    slow = 2
    fast = 2

    while fast < n :
        if nums[slow-2] != nums[fast]:
            nums[slow] = nums[fast]
            slow += 1

        fast +=1
    return slow





print(removeDuplicates([1,1,1,2,2,2,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,4,5,5,5]))
