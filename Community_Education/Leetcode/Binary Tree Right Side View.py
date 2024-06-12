
class Solution(object):
    def rightSideView(self, root):
        if not root: return []
        rView = []
        queue = [root]
        while queue:
            level = []
            size = len(queue)
            for _ in range(size):
                node = queue.pop(0)
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            rView.append(level[-1])
        return rView
