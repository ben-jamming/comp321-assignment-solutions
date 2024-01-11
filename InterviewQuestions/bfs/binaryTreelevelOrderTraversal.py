# Easy
# Passes all test cases

from collections import deque

class TreeNode:
 def __init__(self, val):
   self.val = val
   self.left, self.right = None, None

class Solution:
  def traverse(self, root):
    result = []
    if not root:
        return result

    unvisited_nodes = deque([root]) # add initial children

    while len(unvisited_nodes) > 0:
        level_nodes = [] # add this to result
        level_size = len(unvisited_nodes) # get the number of nodes at this level
        for _ in range(level_size):
            node = unvisited_nodes.popleft()     
            level_nodes.append(node.val)
            if node.left: # Check the left node
                unvisited_nodes.append(node.left)
            if node.right: # Check the right node
                unvisited_nodes.append(node.right)

        result.append(level_nodes)

    return result