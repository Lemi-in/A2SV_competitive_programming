class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        l, r = 0, int(c ** 0.5)  
        while l <= r: 
            sumSquare = l * l + r * r 
            if sumSquare == c:
                return True
            elif sumSquare < c:
                l += 1
            else:
                r -= 1
        return False
