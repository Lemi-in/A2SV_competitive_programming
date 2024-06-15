class Solution:
    def triangleNumber(self, nums):
        nums.sort()
        count = 0
        for i in range(len(nums) - 1, 1, -1):
            c = nums[i]
            a, b = 0, i - 1  
            while a < b:
                if nums[a] + nums[b] > c:
                    count += (b - a)
                    b -= 1
                else: a += 1   
        return count
