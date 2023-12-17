# Easy
# Passess all test cases
class Solution:
  
  def search(self,arr, key):
    import bisect
    if key not in arr:
      return -1
    
    if len(arr) == 1:
      return 0

    def binary_search(arr,key):
        start = 0 
        end = len(arr) - 1 
        ascending_order = arr[start] < arr[end]

        while start <= end:
            mid = start + (end - start) // 2
            mid_val = arr[mid]

            if mid_val ==  key:
                return mid

            if ascending_order:
                if mid_val < key:
                    start = mid + 1 # Must be in left subarray

                else:
                    end = mid - 1 # Must be in right

            else: # this is in the modified version
                if mid_val > key:
                    start = mid + 1

                else:
                    end = mid - 1


    return binary_search(arr,key)

if __name__ == "__main__":
    s = Solution()
    print(s.search([10, 6, 4], 4))  # Output should be 2
    print(s.search([1, 2, 3, 4, 5, 6, 7], 5))  # Output should be 4
    print(s.search([10, 6, 4], 10))  # Output should be 0
    print(s.search([4, 6, 10], 10))  # Output should be 2