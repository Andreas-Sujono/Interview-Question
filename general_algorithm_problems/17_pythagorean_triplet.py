import math
def findPythagoreanTriplets(nums):
    # Fill this in.
    hash = {}
    for num in nums:
        if num in hash:
            hash[num] += 1
        else:
            hash[num] = 1
    length = len(nums)
    for i in range(length-1):
        a = nums[i]
        for j in range(i+1,length):
            b = nums[j]
            if(int(math.sqrt(a**2+b**2)) in hash):
                return True 
    return False
    

print findPythagoreanTriplets([3, 12, 5, 13])
# True