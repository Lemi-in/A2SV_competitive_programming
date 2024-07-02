class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        arr  = []
        n = len(nums)
        i = 0
        while i < n:
            corr = nums[i] - 1
            if nums[i] != nums[corr]:
                nums[i] ,nums[corr] = nums[corr], nums[i]
            else:
                i += 1
        for i in range(n):
            if nums[i] - 1 != i :
                arr.append(i + 1)
        return arr
