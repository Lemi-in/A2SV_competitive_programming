class Solution(object):
    def findMiddleIndex(self, nums):
        n = len(nums)
        prefixL = [0] * n
        prefixR = [0] * n
        
        # Compute prefix sum from the left
        prefixL[0] = nums[0]
        for i in range(1, n):
            prefixL[i] = prefixL[i - 1] + nums[i]
        
        # Compute prefix sum from the right
        prefixR[n - 1] = nums[n - 1]
        for i in range(n - 2, -1, -1):
            prefixR[i] = prefixR[i + 1] + nums[i]
        
        # Check for the middle index
        for i in range(n):
            if prefixL[i] == prefixR[i]:
                return i
        
        return -1
