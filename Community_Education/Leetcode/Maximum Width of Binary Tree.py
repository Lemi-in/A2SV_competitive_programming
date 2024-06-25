class Solution(object):
    def widthOfBinaryTree(self, root):
        #Iterative Solution
        if not root: return 0
        q = deque([(root, 0)])
        mx = 0
        while q:
            n = len(q)
            level = q[0][1]
            for _ in range(n):
                node , idx = q.popleft()
                if node.left:
                    q.append((node.left, idx * 2))
                if node.right:
                    q.append((node.right, idx * 2 + 1))
            mx = max(mx , idx - level + 1)
        return mx

        #Recursive Solution
        level = {}
        width = 0
        def dfs(node,depth, idx):
            if not node: return
            if depth not in level:
                level[depth] = (idx,idx)
            else:
                level[depth] = (level[depth][0], idx)

            dfs(node.left, depth + 1, idx * 2)
            dfs(node.right, depth + 1, idx * 2 + 1)

        dfs(root,0,0)
        for mn , mx in level.values():
            width = max(width , mx - mn + 1)

        return width


