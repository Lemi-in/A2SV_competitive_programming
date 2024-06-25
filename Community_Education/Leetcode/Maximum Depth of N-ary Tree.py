class Solution(object):
    def maxDepth(self, root):
        def dfs(node):
            if not node: return 0
            mx = 0
            for c in node.children:
                mx = max(mx ,dfs(c))
            return 1 + mx
        return dfs(root)

        
