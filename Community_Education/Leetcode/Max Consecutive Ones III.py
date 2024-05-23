class Solution(object):
    def longestOnes(self, nums, k):
        maxWin = zeros = l = 0
        n = len(nums)
        for w in range(n):
            if nums[w] == 0:
                zeros += 1
            while zeros > k:
                if nums[l] == 0:
                    zeros -= 1
                l += 1
            maxWin = max(maxWin , (w - l + 1))
        return maxWin
