class Solution(object):
    def combinationSum(self, candidates, target):
        res = []
        def dfs(nums, target, path):
            if target < 0: return 
            if target == 0:
                res.append(path)
                return 
            for i in range(len(nums)):
                dfs(nums[i:], target-nums[i], path+[nums[i]])
                
        dfs(candidates, target, [])
        return res
