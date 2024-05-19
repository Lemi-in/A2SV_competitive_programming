class Solution(object):
    def maxIceCream(self, costs, coins):
        costs.sort()
        total_sum, count = 0, 0
        i = 0
        while i < len(costs):
            total_sum += costs[i]
            if total_sum > coins:
                return count
            else:
                count += 1
            i += 1

        return count
