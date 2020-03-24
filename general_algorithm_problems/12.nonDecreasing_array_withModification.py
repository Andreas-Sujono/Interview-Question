'''
You are given an array of integers in an arbitrary order. 
Return whether or not it is possible to make the array 
non-decreasing by modifying at most 1 element to any value.

We define an array is non-decreasing if array[i] <= array[i + 1] 
holds for every i (1 <= i < n).
'''

def check(arr):
    # Fill this in.
    length = len(nums)
    counter = 0
    currentMax =-1
    for i in range(0,length-1):
        if(nums[i] > nums[i+1]): # if decreasing
            counter += 1
            if(min(nums[i],nums[i+1]) < currentMax):
                nums[i] = nums[i+1] = max(nums[i],nums[i+1])
            else:
                nums[i] = nums[i+1] = min(nums[i],nums[i+1])
            if(counter == 2):
                return False
        if(nums[i] > currentMax):
            currentMax = nums[i]
    return True if counter <= 1 else False


print check([13, 4, 7])
# True
print check([5,1,3,2,5])
# False
print(check([3,4,2,3]))
#false