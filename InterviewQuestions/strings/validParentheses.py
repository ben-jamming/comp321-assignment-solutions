# Easy
# Passes all test cases
# Good example of stack problem
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        for c in s:
            if c in mapping:
                # Closing bracket
                if not stack or stack[-1] != mapping[c]:
                    return False
                stack.pop()
            else:
                # Opening bracket
                stack.append(c)

        return len(stack) == 0