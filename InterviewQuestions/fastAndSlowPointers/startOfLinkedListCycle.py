# Medium

class Node:
 def __init__(self, value, next=None):
   self.val = value
   self.next = next
   
class Solution:
    def findCycleStart(self,head):
        table = {} # Node: num parents. Note: this approach is more space demanding
        def nonCycleSize(head, length):
            while curr != head:
                size+=1
                curr = curr.next
            return size
        
        def cycleSize(slow, cycle_length):
            
            slow = head
            fast = head
            while fast != None and fast.next != None:
                fast = fast.next.next
                slow = slow.next
                if fast == slow:
                    break
        
        return nonCycleSize(head, fast)
        return slow