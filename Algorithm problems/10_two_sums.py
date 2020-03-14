def two_sum(arr, k):
    # Fill this in.
    hashmap = {}
    for i in arr:
        if(k-i in hashmap):
            return True
        if(i in hashmap):
            hashmap[i] += 1
        else:
            hashmap[i] = 1
    return False
    

print two_sum([4,7,1,-3,2], 5)
# True