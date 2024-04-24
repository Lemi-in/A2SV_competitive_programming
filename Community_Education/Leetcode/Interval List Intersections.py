class Solution:
    def intervalIntersection(self, first: List[List[int]], second: List[List[int]]) -> List[List[int]]:
       
        first.sort()
        second.sort()
        l = 0
        r = 0
        ans = []
        while l < len(first) and r < len(second):
            min_l = first[l][0]
            max_l = first[l][1]
            min_r = second[r][0]
            max_r = second[r][1]
            if min_l <= max_r <= max_l or min_r <= max_l <= max_r:
                left = max(min_l,min_r)
                right = min(max_l,max_r)
                ans.append((left,right))
            if max_r <= max_l:
                r += 1
            else:
                l += 1
        return ans
