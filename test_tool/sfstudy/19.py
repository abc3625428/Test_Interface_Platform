

def containsNearbyDuplicate(nums, k):

    # for i in range(len(nums)-1):
    #     for j in range(i+1,len(nums)):
    #         if nums[i] == nums[j] and abs(i-j) <= k:
    #             return True
    # return False

    l = 0
    r = len(nums)
    re = {}
    while l <= r:
        print(re)
        if nums[l] not in re:
            re[nums[l]]=l
            l+=1
        elif nums[l] in re and abs(l-re[nums[l]]) <= k:

            return True
        else:
            re[nums[l]] = l
            l+=1

    return False




print(containsNearbyDuplicate([1,0,1,1],1))