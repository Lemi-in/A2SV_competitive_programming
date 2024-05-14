# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        oddHead = head
        evenHead = head.next
        odd = oddHead
        even = evenHead
        
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        
        #we connect the two 
        odd.next = evenHead
        return oddHead
