def staircase(n):
    # Fill this in.
    if(n == 2):
        return 2
    elif n == 1:
        return 1
    else:
        return staircase(n-1) + staircase(n-2)

# def staircase(n):
#     if (n == 0):
#         return 0
#     if (n == 1):
#         return 1
#     if ( n == 2):
#         return 2
    
#     output = 0
#     output1 = 1
#     output2 = 2
#     for i in range(2,n):
#         output = output1+output2
#         output1 = output2
#         output2 = output

#     return output


print staircase(4)
# 5
print staircase(38)
# 8