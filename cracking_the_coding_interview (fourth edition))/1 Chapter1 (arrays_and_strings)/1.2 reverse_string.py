def reverseString(s):
    return s[-1::-1]
# alternative solution
# 1) additional variable, copy letter from behind
# 2) swap last pointer and first pointer
# 

print(reverseString('12345'))