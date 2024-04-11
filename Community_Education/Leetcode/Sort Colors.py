class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        x,y, curr = 0,len(nums) - 1,0
        while curr <= y: 
            if nums[curr] ==0:  
                nums[x], nums[curr] = nums[curr], nums[x]
                x += 1
                curr += 1
            elif nums[curr] ==2:  
                nums[y], nums[curr] = nums[curr], nums[y]
                y -= 1
            else:
                curr += 1 
