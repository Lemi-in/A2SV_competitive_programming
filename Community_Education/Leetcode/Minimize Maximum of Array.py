class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        n = len(nums)
        pre = [0] * (n + 1)
        for i in range(n):
            pre[i + 1] = pre[i] + nums[i]

        res = float('-inf')
        for i in range(1, n + 1):        
            avg = math.ceil(pre[i] / i)
            res = max(res, avg)
            
        return res
