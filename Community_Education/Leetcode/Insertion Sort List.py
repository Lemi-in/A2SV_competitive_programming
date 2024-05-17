class Solution(object):
    def insertionSortList(self, head):

        sortedL = ListNode(0)
        curr = head

        while curr:
            value = curr.val
            nxt = curr.next
            prev = sortedL

            while prev.next and prev.next.val < value:
                prev = prev.next
            
            curr.next , prev.next , curr = prev.next , curr, nxt

        return sortedL.next
