# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right: 
            return head

        dummy = ListNode(0,next=head)
        prev = dummy
        n = 1

        while n < left:
            prev = prev.next
            n += 1

        curr = prev.next
        i = 0
        while i < right - left:
            temp = curr.next
            curr.next = temp.next
            temp.next = prev.next
            prev.next = temp
            i += 1
        return dummy.next

        
