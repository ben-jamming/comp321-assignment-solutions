# Easy
# Passes all cases
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        table = {}

        for i, n in enumerate(nums):
            diff = target - n

            if diff in table:
                return table[diff], i

            table[n] = i

        return []