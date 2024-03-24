class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        multi = 2 * n
        if n % 2 == 0:
            return n
        else:
            return multi
