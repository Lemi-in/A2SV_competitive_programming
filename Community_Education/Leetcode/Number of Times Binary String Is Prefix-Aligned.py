class Solution(object):
    def numTimesAllBlue(self, flips):
        n = len(flips)
        count = 0
        maxx = 0

        for i in range(n):
            maxx = max(maxx, flips[i])
            if maxx == i + 1:
                count += 1
                
        return count
