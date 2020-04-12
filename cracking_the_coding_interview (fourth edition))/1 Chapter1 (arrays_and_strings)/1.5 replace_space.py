def replaceSpace(s):
    #return s.replace(' ','%20')
    i = 0
    while(i < len(s)):
        if s[i] ==" ":
            s = s[:i] + '%20' + s[i+1:]
            i += 2
        i += 1
    return s

#  alternative solution
#  1) use replace
#  2) inplace, using loop
# 

print(replaceSpace(' h h h    '))