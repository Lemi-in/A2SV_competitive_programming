class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        x , y = 0 , n - 1
        i , j = -1, -1
        while x <= y:
            mid = (x + y) // 2
            if nums[mid] == target:
                j = mid
                y = mid - 1
            elif nums[mid] < target:
                x = mid + 1
            else:
                y = mid - 1
        x, y = 0, n - 1
        while x <= y:
            mid = (x + y) // 2
            if nums[mid] == target:
                i = mid
                x = mid + 1
            elif nums[mid] < target:
                x = mid + 1
            else:
                y = mid - 1
        
        return [j, i]
