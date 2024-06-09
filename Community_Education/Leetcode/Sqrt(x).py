class Solution(object):
    def mySqrt(self, x):
        l , r = 1 , x
        while l <= r:
            mid = (l + r) // 2
            sqrt = mid * mid
            if sqrt == x:
                return mid
            elif sqrt < x:
                l = mid + 1
            else:
                r = mid - 1
        return r
      
