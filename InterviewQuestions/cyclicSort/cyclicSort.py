# Easy
# Passes all test cases
class Solution:
    def sort(self, nums):
        n = 1
        while n < len(nums) + 1:
            prev_spot = nums.index(n)
            nums[prev_spot] = nums[n-1]
            nums[n-1] = n
            n+=1
        return nums

s = Solution()
print(s.sort([3,1,5,4,2]))