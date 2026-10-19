# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        valSet = set()
        value = head
        if not head:
            return False 
        
        while value.next: 
            if value.val in valSet: 
                return True 
            else: 
                valSet.add(value.val)
            value = value.next
        return False
        



        