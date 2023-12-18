# Without repeating characters
# Medium
# Passes all test cases
class Solution:

    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = {}
        longest = 0
        front = 0
        end = len(s) - 1
        for back in range(len(s)):
            if s[back] in chars:
                front = max(front, chars[s[back]] + 1)

            chars[s[back]] = back
            longest = max(back - front + 1, longest)

        return longest