
class Node:
    def __init__(self, value, next=None):
        self.val = value
        self.next = next

class Solution:
    def reverse(self, head):
        result = None
        if head.next == None or head == None:
            return head
        nxt = None
        dummy = head
        previous = None
        while dummy: 
            nxt = dummy.next # dummy -> 4
            dummy.next = previous # dummy -> 4 -> 2
            previous = dummy # previous = dummy -> 4 -> 2
            dummy = nxt # 
            
        return previous
