class Solution(object):
    def partition(self, head, x):
        small = cur1 = ListNode()
        big = cur2 = ListNode()
        while head:
            if head.val < x:
                cur1.next = head
                cur1 = cur1.next
            else:
                cur2.next = head
                cur2 = cur2.next
            head = head.next
        cur2.next ,cur1.next = None, big.next
        return small.next
