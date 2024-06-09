class Solution(object):
    def mergeTrees(self, root1, root2):
        #recursive way
        if not root1 and not root2: return None
        if not root1: return root2
        if not root2: return root1

        merged = TreeNode(root1.val + root2.val)
        merged.left = self.mergeTrees(root1.left, root2.left)
        merged.right = self.mergeTrees(root1.right, root2.right)
        return merged

        #iterative way
        q = deque([(root1, root2)])
        while q:
            node1 , node2 = q.popleft()
            node1.val += node2.val
            if node1.left and node2.left:
                q.append((node1.left, node2.left))
            elif not node1.left:
                node1.left = node2.left
            if node1.right and node2.right:
                q.append((node1.right, node2.right))
            elif not node1.right:
                node1.right = node2.right
        return root1
