# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def swapNodes(self, head, k):
        begin = end = head
        i = 1
        while i < k:
            begin = begin.next
            i += 1

        temp = begin
        while temp and temp.next:
            temp = temp.next
            end = end.next
        begin.val, end.val = end.val, begin.val

        return head
