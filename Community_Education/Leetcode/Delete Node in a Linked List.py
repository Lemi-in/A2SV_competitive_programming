# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        if node.next is not None:
            node.val = node.next.val
            node.next = node.next.next
        else:
            itr = node
            while itr:
                if itr.next.next is None:
                    itr.next = None
                    break
                itr = itr.next

        
