# Easy
# Passes all test cases
class Solution:
  def findMaxSumSubArray(self,k, arr):
    max_sum = -1
    for i in range(len(arr)):
      if i + k > len(arr):
        return max_sum

      max_sum = max(sum(arr[i:i+k]), max_sum)
      
    return max_sum