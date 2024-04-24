class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort()
        operation = 0
        step = 0
        i = 1 
        while i < len(nums):
            if nums[i] > nums[i - 1]:
                step += 1
                operation += step
            else:
                operation += step
            i += 1  
        return operation
