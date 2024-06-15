class Solution(object):
    def minMoves(self, t, m):
        cnt = 0
        while m > 0 and t > 1:
            if t % 2 == 0:
                t = t/2
                m -= 1
            else: 
                t -= 1
            cnt += 1
        return cnt + t - 1
