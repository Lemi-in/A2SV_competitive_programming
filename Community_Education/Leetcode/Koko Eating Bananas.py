class Solution(object):
    def minEatingSpeed(self, piles, h):
        l, r = 1, max(piles)
        while l < r:
            mid = (l + r) // 2
            t = sum((p - 1) // mid + 1 for p in piles)
            if h >= t:
                r = mid
            else:
                l = mid + 1

        return l
