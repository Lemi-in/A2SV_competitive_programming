class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        i = 0
        n = len(nums)
        while i < n:
            if nums[i] != i + 1:
                current = nums[i] - 1
                if nums[i] != nums[current] :
                    nums[current] , nums[i] = nums[i],nums[current]
                else:
                    return nums[i]
            else:
                i += 1
    
