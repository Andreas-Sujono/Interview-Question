def is_anagram(s1,s2):
    arr = [0]*256
    for i in s1:
        arr[ord(i)] += 1
    
    for j in s2:
        if(arr[ord(j)] <= 0):
            return False
        arr[ord(j)] -= 1
    return True


# alternative solution
# 1) sort 2 string, check if both identical
# 2) use hashmap
# 3) use array with 256 length

print(is_anagram('carc','racc'))