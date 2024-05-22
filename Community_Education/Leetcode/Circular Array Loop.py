class Solution(object):
    def circularArrayLoop(self, nums):
        n = len(nums)
        seen = set()
        for i in range(n):
            if i not in seen:
                cycle = set()
                while True:
                    if i in cycle:
                        return True
                    seen.add(i)
                    cycle.add(i)
                    prev , i = i , (i + nums[i])%n
                    if prev == i:
                        break
                    if (nums[prev] > 0 and nums[i] < 0) or (nums[prev] < 0 and nums[i] > 0):
                        break
        return False
        
