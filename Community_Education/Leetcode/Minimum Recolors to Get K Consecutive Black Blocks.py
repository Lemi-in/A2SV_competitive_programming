class Solution(object):
    def minimumRecolors(self, blocks, k):
        n = len(blocks)
        l = 0
        minsub = float("inf")
        cntW = 0
        for r in range(n):
            if blocks[r] == "W":
                cntW += 1
            if (r - l + 1) == k:
                minsub = min(minsub, cntW)
                if blocks[l] == "W":
                    cntW -= 1
                l += 1
        return minsub
            
