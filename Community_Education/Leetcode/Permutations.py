class Solution(object):
    def permute(self, nums):
        def dfs(nums, path, res):
            if not nums:
                res.append(path)
                return 
            for i in range(len(nums)):
                dfs(nums[:i] + nums[i+1:],path + [nums[i]] , res)
        res = []
        dfs(nums, [], res)
        return res

