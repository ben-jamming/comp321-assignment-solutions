# Easy
# Passes all test cases

class Node:
 def __init__(self, value, next=None):
   self.val = value
   self.next = next

class Solution:
  def hasCycle(self, head):
    slow = head
    fast = head.next
    while fast != None:
        if slow.val == fast.val:
            return True

        
        slow = slow.next
        if fast.next == None or fast.next.next == None:
            break
        for _ in range(2):
            fast = fast.next
  
    return False