class Solution(object):
    def levelOrder(self, root):
        #Iterative way
        if not root: return []
        result = []
        queue = deque([root])
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level)
        return result

        # Recursive way
        def helper(node, level):
            if not node:
                return
            if len(result) == level:
                result.append([])
            result[level].append(node.val)
            helper(node.left, level + 1)
            helper(node.right, level + 1)
        
        result = []
        helper(root, 0)
        return result
