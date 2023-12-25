# Easy
# Passes all test cases
class Solution:
    def makeSquares(self, arr):
        n = len(arr)
        squares = [0 for x in range(n)]
        start, end = 0, n - 1
        highest = n-1
        while start <= end:
            r = arr[end] * arr[end]
            l = arr[start] * arr[start]
            if l > r:
                squares[highest] = l
                start+=1
            else:
                squares[highest] = r
                end -= 1
            highest -= 1
        return squares

if __name__ == "__main__":
    s = Solution()
    print(s.makeSquares([-2, -1, 0, 2, 3]))