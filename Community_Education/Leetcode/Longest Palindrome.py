class Solution(object):
    def longestPalindrome(self, s):
        n = len(s)
        if n == 0: return 0
        if n == 1: return 1
        mapp = Counter(s)
        if n == 2 and len(mapp) == 1: return 2
        cnt = 0
        toggle = False
        if len(mapp) == 1:
            return len(s)
        for x, y in mapp.items():
            if y % 2 ==  1:
                toggle = True
            if y % 2 == 0:
                cnt += y
            else:
                cnt += y - 1
        
        return cnt + 1 if toggle else cnt
