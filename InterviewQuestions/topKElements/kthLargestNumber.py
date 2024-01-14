# Easy
# Passes all test cases
from heapq import *

class Solution:
  def findKthSmallestNumber(self, nums, k):
    if k == 1:
      return min(nums)
    h = []
    for i in range(len(nums)):
      if len(h) < k:
        heappush(h, -nums[i])
      
      else:
        if -h[0] > nums[i]:
          heappop(h)
          heappush(h, -nums[i])
      print(h)
    return -h[0]
