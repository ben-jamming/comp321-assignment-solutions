# Easy
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
  def hasPath(self, root, sum):
    if not root:
        return False
    
    if root.val == sum and root.left is None and root.right is None:
        return True
    
    return self.hasPath(root.left, sum - root.val) or self.hasPath(root.left, sum - root.val)