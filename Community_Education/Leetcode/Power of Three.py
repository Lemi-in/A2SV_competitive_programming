class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        def check(num):
            if num == 1:
                return True
            if num < 1 or num % 3 != 0:
                return False
            return check(num // 3)
        
        return check(n)
