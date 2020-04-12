'''
    given a string, check if a string has all unique char
    Note: cannot use additional data structure
'''
def isUniqueChar(string):
    string2 =  ''.join(set(list(string)))
    print(string2)
    return len(string) == len(string2)

# Alternative solution
# 1) use hashmap and check if particular letter appears at least twice
# def isUniqueChar(string):
#     hashmap = {}
#     for x in string:
#         for x in hashmap:
#             return False
#         hashmap[x] = 1
#     return True
# 
# 2) sort letter , check if there are same letter adjacent --> sort letter by change to list first, byusing sorted()
# 3) best answer: use bitwise manipulation, for every char converted to ASCII,
#    leftshifted 1 by that number, if there is other 1 shifted in same location, return False

print( isUniqueChar('abcdeff'))