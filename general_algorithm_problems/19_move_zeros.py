class Solution:
    def moveZeros(self, nums):
        # Fill this in.
        pointerZero = 0
        length = len(nums)
        for i in range(0,length):
            if(nums[i] != 0):
                #swap with pointerZero
                nums[pointerZero], nums[i] = nums[i], nums[pointerZero]
                pointerZero += 1
        return nums


nums = [0, 0, 0, 2, 0, 1, 3, 4, 0, 0]
Solution().moveZeros(nums)
print(nums)
# [2, 1, 3, 4, 0, 0, 0, 0, 0, 0]

nums = [0,1,0,3,12]
Solution().moveZeros(nums)
print(nums)