class Solution(object):
    def subsetsWithDup(self, nums):
        def dfs(nums, index, path, res):
            #Backtracking
            res.add(tuple(path))
            for i in range(index, len(nums)):
                dfs(nums, i + 1, path + [nums[i]], res)

        res = set()
        dfs(sorted(nums), 0, [], res)
        return res
