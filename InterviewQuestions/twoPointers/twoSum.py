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

# If array is sorted
# class Solution:
#   def search(self, arr, target_sum):
#     small, large = 0, len(arr) - 1
#     table = {}
#     while small < large:
#       if arr[small] + arr[large] == target_sum:
#         return [small, large]

#       if arr[small] + arr[large] < target_sum:
#         small+=1
      
#       else:
#         large-=1

#     return [-1,-1]