class Solution:
    def detectCycle(self, head):
        if head is None or head.next is None:
            return None  
        fast = slow = temp = head
        while fast.next is not None and fast.next.next is not None:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                while temp != slow:
                    temp = temp.next
                    slow = slow.next
                return slow
        return None
