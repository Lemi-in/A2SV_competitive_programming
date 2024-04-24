class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        
        mini = float('inf')
        win = 0
        left = 0
        
        for right in range(n):
            win += nums[right]
            
            while win >= target:
                mini = min(mini, right - left + 1)
                win -= nums[left]
                left += 1
        
        return mini if mini != float('inf') else 0
