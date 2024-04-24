class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()  
        n = len(nums)
        closest = float('inf')
        i = 0
        while i < n - 2:
            left = i + 1
            right = n - 1
            
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if abs(total - target) < abs(closest - target):
                    closest = total
                if total < target:
                    left += 1
                elif total > target:
                    right -= 1
                else:
                    return closest
            i += 1
            
        return closest
