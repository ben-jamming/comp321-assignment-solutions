# Easy
# Passes all test cases
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None:
            return root
        left = self.invertTree(root.right)
        right = self.invertTree(root.left)

        root.left, root.right = left, right

        return root