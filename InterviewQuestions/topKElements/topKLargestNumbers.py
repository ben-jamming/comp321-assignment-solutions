# Easy
# Passes all test cases
from heapq import *

class Solution :
  def findKLargestNumbers(self, nums, k):
    min_heap = []
    for i in range(k): # k log k
      heappush(min_heap, nums[i]) 

    for i in range(k, len(nums)): # (n - k) * log k
      if nums[i] > min_heap[0]:
        heappop(min_heap)
        heappush(min_heap, nums[i])

    return min_heap # O(k log k + (n - k) log k) == O(n log k)

    