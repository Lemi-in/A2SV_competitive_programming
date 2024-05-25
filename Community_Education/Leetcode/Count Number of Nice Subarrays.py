class Solution(object):
    def numberOfSubarrays(self, nums, k):
        l , r = 0 , 0
        count , odds = 0 , 0
        total = 0

        while r < len(nums):
            if nums[r] % 2 != 0 :
                count += 1
                odds = 0
            while count == k :
                if nums[l] % 2 != 0:
                    count -= 1
                odds +=1
                l += 1
            total += odds 
            r += 1
        return total
