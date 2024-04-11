class Solution:
    def isPalindrome(self, x: int) -> bool:
        revstr = str(abs(x))[::-1]
        revint = int(revstr)

        if x == revint:
            return True
        else:
            return False
