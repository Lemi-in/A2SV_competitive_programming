class Solution(object):
    def maximumUniqueSubarray(self, nums):
        seen = set()
        maxSum = 0
        currSum = 0
        l = 0
        for r in range(len(nums)):
            while nums[r] in seen:
                seen.remove(nums[l])
                currSum -= nums[l]
                l += 1
            seen.add(nums[r])
            currSum += nums[r]
            maxSum = max(maxSum, currSum)
        
        return maxSum
