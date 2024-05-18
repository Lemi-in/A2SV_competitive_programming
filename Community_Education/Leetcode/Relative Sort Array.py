class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        mapp = Counter(arr1)
        ans = []
        for val in arr2:
            if val in mapp:
                count = mapp.pop(val)
                ele = [val] * count  
                ans.extend(ele)  
        
        rem = []
        for key, count in mapp.items():
            rem.extend([key] * count)
        rem.sort()
        ans.extend(rem)
        return ans
