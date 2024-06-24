class Solution:
    def subsets(self, nums):
        def dfs(nums, index, path, res):
            #Backtracking
            res.append(path)
            for i in range(index, len(nums)):
                dfs(nums, i + 1, path + [nums[i]], res)

        res = []
        dfs(sorted(nums), 0, [], res)
        return res
