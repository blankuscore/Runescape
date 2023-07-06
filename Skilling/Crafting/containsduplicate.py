def cduplicate(nums):
    temp = nums
    truecount = 0
    for k in nums:
        for h in temp:
            if(k == h):
                truecount = truecount + 1
    if truecount > len(nums): 
        return True
    else:
        return False
    

print("Truecount is {}".format(cduplicate([1,1,1,3,3,4,3,2,4,2])))