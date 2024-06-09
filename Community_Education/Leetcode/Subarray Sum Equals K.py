class Solution:
    def subarraySum(self, nums, k):
       mapp = {}
       mapp[0] = 1
       summ , count = 0 , 0
       
       for i in range(len(nums)):
           summ += nums[i]
           if summ-k in mapp: 
               count += mapp[summ-k]
           if summ in mapp:
               mapp[summ] += 1
           else:
               mapp[summ] = 1
       
       return count
   	
