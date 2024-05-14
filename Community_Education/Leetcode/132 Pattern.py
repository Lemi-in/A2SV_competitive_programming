class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 3:
            return False
        stack = []
        secondMax = float ('-inf')

        for i in range(n-1, -1, -1):  
            if nums[i] < secondMax:
                return True
            while stack and stack[-1] <  nums[i]:
                secondMax = stack.pop()
            stack.append(nums[i])
        return False

       
