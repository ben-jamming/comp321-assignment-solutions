# Medium
# Passes all test cases
class Solution:
    def searchCeilingOfANumber(self, arr,key):
        start = 0
        end = len(arr) - 1
        if key > arr[-1]:
            return -1
        smallest = len(arr) - 1
        while start <=  end:
            mid = start + (end- start) // 2
            if key == arr[mid]:
                return mid
            
            elif arr[mid] < key:
                start = mid + 1

            else:
                end = mid - 1
                smallest = mid

        return smallest
    
if __name__ == "__main__":
    s = Solution()
    print(s.searchCeilingOfANumber([4, 6, 10], 10))
    print(s.searchCeilingOfANumber([1, 3, 8, 10, 15], 12))
    print(s.searchCeilingOfANumber([4, 6, 10], 17))
    print(s.searchCeilingOfANumber([4, 6, 10], -1))

                

