# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            prev = slow
            slow = slow.next
        return slow
        
