def singleNumber(nums):
    # Fill this in.
    hashmap = {}
    for num in nums:
        if(num in hashmap):
            hashmap[num] += 1
        else:
            hashmap[num] = 1
    
    for key in hashmap:
        if(hashmap[key] == 1):
            return key
            
    return -1 # not found
          

print singleNumber([4, 3, 2, 4, 1, 3, 2])
# 1