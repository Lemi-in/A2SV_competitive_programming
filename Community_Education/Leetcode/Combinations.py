class Solution:
    def combine(self, n, k):
        def backtrack(start, path, res):
            if len(path) == k:
                res.append(path[:])
                return
            i = start
            while i <= n:
                path.append(i)
                backtrack(i + 1, path, res)
                path.pop()  # backtrack
                i += 1

        res = []
        backtrack(1, [], res)
        return res
