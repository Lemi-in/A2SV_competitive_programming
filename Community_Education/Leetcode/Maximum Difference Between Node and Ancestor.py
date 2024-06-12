class Solution(object):
    def maxAncestorDiff(self, root):
        #iterative way
        diff = 0
        q = deque([(root, root.val, root.val)])
        while q:
            node , cmx , cmn = q.popleft()
            print(node.val)
            diff = max(diff, cmx - cmn)
            if node.left:
                q.append((node.left, max(cmx, node.left.val), min(cmn, node.left.val)))
            if node.right:
                q.append((node.right, max(cmx, node.right.val), min(cmn, node.right.val)))
        return diff

        #recursive way
        def dfs(node, mn , mx):
            if not node: 
                return mx - mn
            mn = min(mn, node.val)
            mx = max(mx, node.val)
            return max(dfs(node.left,mn, mx), dfs(node.right, mn , mx))
            
        return dfs(root, root.val, root.val)
