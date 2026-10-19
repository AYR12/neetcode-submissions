# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
        #trouver la moitié : 
        slow = head 
        fast = head.next 
        while fast and fast.next:
            slow  = slow.next
            fast = fast.next.next

        second = slow.next 
        slow.next = None 

        prev = None 
        current = second 
        while current:
            temp = current.next #sauvegarde prochain noeux 
            current.next = prev # inverse le lien
            prev = current #prev avance
            current = temp #curr avance dans l'ancienne liste 

        first, second = head, prev
        while second: 
            tmp1, temp2 = first.next, second.next 
            first.next = second
            second.next = tmp1
            first, second = tmp1, temp2

