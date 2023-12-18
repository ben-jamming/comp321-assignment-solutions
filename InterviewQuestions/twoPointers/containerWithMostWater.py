# Also a greedy problem
# Medium
# Passes all test cases
class Solution:
    def maxArea(self, height: List[int]) -> int:
        start, end = 0, len(height) - 1
        max_size = 0
        while start < end:
            max_size = max(min(height[start], height[end]) * (end - start), max_size)
            if height[start] > height[end]:
                end -= 1
            else:
                start += 1

        return max_size