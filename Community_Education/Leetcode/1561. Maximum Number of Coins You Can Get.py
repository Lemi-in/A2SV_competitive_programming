class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)  
        n = len(piles)
        mycoins = 0
        i = 1
        while i < n / 3 * 2:  
            mycoins += piles[i]
            i += 2
        return mycoins
