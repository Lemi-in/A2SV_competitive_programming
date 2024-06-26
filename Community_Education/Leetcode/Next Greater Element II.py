class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [-1] * n
        stack = []
        
        # go through the array twice to simulate the circular behavior
        # found it out the hard way 
        for _ in range(2):
            for i in range(n-1, -1 , -1):
                while stack and stack[-1] <= nums[i]:
                    stack.pop()
                if not stack:
                    ans[i] = -1
                else:
                    ans[i] = stack[-1]
                stack.append(nums[i])
        return ans
