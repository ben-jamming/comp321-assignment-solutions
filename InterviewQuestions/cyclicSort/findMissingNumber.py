class Solution:
    def findMissingNumber(self, nums):
        n = len(nums)
        i = 0
        while i < n:
            j = nums[i]
            if nums[i] < n and nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            
            else:
               i+=1
               
        for num in range(n):
            if nums[num] != num:
                return num        

        return n