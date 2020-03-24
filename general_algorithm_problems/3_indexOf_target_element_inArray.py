class Solution: 
  def getRange(self, arr, target):
    # Fill this in.
    result = []
    for i in range(0,len(arr)):
        if(len(result) == 2 and arr[i] == target):
            result[1] = i
            continue
        if arr[i] == target:
            result.append(i)
    return result if len(result) == 2 else [-1,-1]
  
# Test program 
arr = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8] 
x = 2
print(Solution().getRange(arr, x))
# [1, 4]

arr = [1,3,3,5,7,8,9,9,9,15]
x = 9
print(Solution().getRange(arr, x))
# [6, 8]

arr = [100, 150, 150, 153]
x = 150
print(Solution().getRange(arr, x))
# [1, 2]

arr = [1,2,3,4,5,6,10]
x = 9
print(Solution().getRange(arr, x))
# [-1,-1]