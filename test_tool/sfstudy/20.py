

def summaryRanges(nums):

    l = r = 0
    n = len(nums)-1
    ls = []
    while l<=n and r <=n:
        if (r+1)>n and nums[r] - nums[r - 1] != 1:
            ls.append(str(nums[r]))
            r+=1
            l=r

        elif (r+1)>n and nums[r] - nums[r - 1] == 1:
            ls.append(str(nums[l])+'->'+str(nums[r]))
            r+=1
            l=r

        else:
            if nums[r+1] - nums[r] ==1:
                r+=1

            elif nums[r+1] - nums[r] !=1 and nums[r] - nums[r-1] !=1:
                ls.append(str(nums[l]))
                r+=1
                l = r
            elif nums[r+1] - nums[r] !=1:
                ls.append(str(nums[l])+'->'+str(nums[r]))
                l=r+1
                r=l
    return ls

print(summaryRanges([0,2,3,4,6,8,9]))