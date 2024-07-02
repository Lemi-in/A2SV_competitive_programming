class Solution(object):
    def missingNumber(self, nums):
        n = len(nums)
        
        i = 0
        while i < n:
            if nums[i] < n and nums[i] != nums[nums[i]]:
                nums[nums[i]], nums[i] = nums[i], nums[nums[i]]
            else:
                i += 1
        
        for i in range(n):
            if nums[i] != i:
                return i
        
        return n
