# Medium

from matplotlib import table


class Solution:
  def searchTriplets(self, arr):
    triplets = []
    table = {}
    if len(arr) < 3:
      if sum(arr) == 0:
        return [arr]
      else:
        return []

    n = len(arr) - 1
    trailing, leading = 1, n
    
    while trailing <= leading:
      print(triplets)
      target_sum = -arr[trailing]
      curr_sum = arr[leading] + arr[trailing]
      
      if target_sum > curr_sum:
        trailing += 1
      
      if diff in table:
          return [arr[trailing], arr[leading], table[diff]]
      
      else:
          table[diff] = arr[leading - trailing]
      trailing+=1
    return triplets

if __name__ == "__main__":
    s = Solution()
    print(s.searchTriplets([-3, 0, 1, 2, -1, 1, -2]))
    #print(s.searchTriplets([-5, 2, -1, -2, 3]))
    #print(s.searchTriplets([1, -2, 1, 0, 5]))
    #print(s.searchTriplets([0, 0, 0, 0]))