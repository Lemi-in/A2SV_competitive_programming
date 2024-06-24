class Solution(object):
    def combinationSum2(self, candidates, target):
        def dfs(nums, ind, path, res, target):
            if target < 0:
                return
            if target == 0:
                res.add(tuple(sorted(path)))
                return
            for i in range(ind, len(nums)):
                if i > ind and nums[i] == nums[i-1]:
                    continue
                dfs(nums, i + 1, path + [nums[i]], res, target - nums[i])
        res = set()
        dfs(sorted(candidates), 0, [], res, target)
        return res
