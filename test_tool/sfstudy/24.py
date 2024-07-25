


def rotate(nums, k):
    n = len(nums)
    s  = k % n
    s1 = nums[0:s]
    s2 = nums[s:len(nums)]

    return s2+s1,s

print(rotate([1,2,3,4,5,6,7],3))


