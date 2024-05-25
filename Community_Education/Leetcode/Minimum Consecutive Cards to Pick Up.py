class Solution(object):
    def minimumCardPickup(self, cards):
        n = len(cards)
        minn = float("inf")
        l = 0
        curr = 0
        seen = set()
        
        for r in range(n):
            while cards[r] in seen:
                seen.remove(cards[l])
                curr = r - l + 1
                minn = min(minn, curr)
                l += 1
            seen.add(cards[r])
            
        return -1 if minn == float("inf") else minn
