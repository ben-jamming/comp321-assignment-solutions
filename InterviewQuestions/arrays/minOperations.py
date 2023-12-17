# Easy
class Solution:
    def minimumOperations(self, nums) -> int:
        nums = [n for n in nums if n > 0]
        if len(nums) == 0:
            return 0
        nums = sorted(nums)
        count = 0
        while len(nums) > 0:
            min_n = min(nums)
            nums = [n-min_n for n in nums if n-min_n > 0]
            count+=1
            

        return count
        

if __name__ == "__main__":
    c = Solution()
    print(c.minimumOperations([1,5,0,3,5]))
    print(c.minimumOperations([0,0,0,0,0,0]))