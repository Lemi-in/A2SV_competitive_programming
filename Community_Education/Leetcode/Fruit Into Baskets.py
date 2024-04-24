
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        container = {}
        total = 0
        l = 0
        r = 0
        while r < len(fruits):
            fruit = fruits[r]
            container[fruit] = r
            if len(container) > 2:
                minIn = min(container.values())
                del container[fruits[minIn]]
                l = minIn + 1
                
            total = max(total, r - l + 1)
            r += 1
        
        return total
