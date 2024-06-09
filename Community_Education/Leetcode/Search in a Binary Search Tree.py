class Solution(object):
    def searchBST(self, root, val):
        #Brute Force Solution
        if root.val == val: return root
        q = deque([root])
        while q:
            node = q.popleft()
            if node.val == val:
                return node
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return None

        #Optimal Solution
        while root != None:
            if val > root.val:
                root = root.right
            elif val < root.val:
                root = root.left
            else:
                return root
        return None
