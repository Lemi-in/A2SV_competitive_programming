class Solution:
    def isCovered(self, ranges, left, right):
        for i in range(left, right + 1):
            isCov = False
            for rang in ranges:
                if rang[0] <= i <= rang[1]: 
                    isCov = True
            if not isCov:
                return False
        return True
