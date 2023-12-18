# Easy
# Passes all test cases
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l1_curr = list1
        l2_curr = list2
        # Merge onto l1
        while l1_curr != None:
            if l1_curr.val > l2_curr.val:
                dummy = l2_curr 

            l1_curr = l1_curr.next