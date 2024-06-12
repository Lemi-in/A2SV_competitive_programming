class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        curr = root
        mn = min(p.val, q.val)
        mx = max(p.val, q.val)
        while curr:
            if curr.val < mn:
                curr = curr.right
            elif curr.val > mx:
                curr = curr.left
            else:
                return curr
        return None
