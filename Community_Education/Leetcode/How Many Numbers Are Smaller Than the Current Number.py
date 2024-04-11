class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        num = sorted(nums)
        arr = []
        for x in nums:
            arr.append(num.index(x))
        return arr

       
