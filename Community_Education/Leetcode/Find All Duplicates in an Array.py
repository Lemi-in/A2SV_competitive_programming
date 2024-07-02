class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        #Optimal Solution 
        n = len(nums)
        i = 0
        arr = []
        while i < n:
            corr = nums[i] - 1
            if nums[i] != nums[corr]:
                nums[i] ,nums[corr] = nums[corr], nums[i]
            else:
                i += 1
        for i in range(n):
            if nums[i] - 1 != i :
                arr.append(nums[i])
        return arr

        #Brute Force
        mapp = Counter(nums)
        arr = []
        for key, val in mapp.items():
            if val == 2:
                arr.append(key)
        return arr
