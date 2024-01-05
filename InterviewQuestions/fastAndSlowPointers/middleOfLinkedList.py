# Easy

from math import ceil


class Node:
 def __init__(self, value, next=None):
   self.val = value
   self.next = next

class Solution:
    def findMiddle(self, head):
        # When fast poiunter reaches the end
        # The slow pointer is the middle
        # Slow pointe rwill be at n/2 and fast will be at n when end is reacged
        fast = head
        slow = head
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
        return slow
