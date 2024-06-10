class Solution(object):
    def isValidBST(self, root):
        if not root: return True
        
        q = deque([(root, float('-inf'), float('inf'))])
        while q:
            node, l, r = q.popleft()
            print(l , r)
            if node.val <= l or node.val >= r:
                return False
            if node.left:
                q.append((node.left, l, node.val))
            if node.right:
                q.append((node.right, node.val, r))
        
        return True
