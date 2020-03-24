def sortNums(nums):
    # by pointer in first and last
    firstPointer = 0
    lastPointer = len(nums)-1
    i = 0
    while(i <= lastPointer):
        if(nums[i] == 1):
            nums[i],nums[firstPointer] = nums[firstPointer],nums[i]
            firstPointer += 1
            i += 1 
        elif(nums[i] == 3):
            nums[i],nums[lastPointer] = nums[lastPointer],nums[i]
            lastPointer -= 1
        else:
            i += 1
    return nums

    #count sort
    # cumulativeSums = [0,0,0]
    # count = [0,0,0]
    # for num in nums:
    #     count[num-1] += 1
    # for i in range(len(count)):
    #     cumulativeSums[i] = (cumulativeSums[i-1] if i > 0 else 0) + count[i]
    
    # result = [0] * len(nums)
    # for i in range(len(nums)-1,-1,-1):
    #     result[cumulativeSums[nums[i]-1] -1 ] = nums[i]
    #     cumulativeSums[nums[i]-1] -= 1
    # return result    
    


print(sortNums([3,2,1,1,2,1,3,2,3]))
# [1, 1, 1, 2, 2, 2, 3, 3, 3]