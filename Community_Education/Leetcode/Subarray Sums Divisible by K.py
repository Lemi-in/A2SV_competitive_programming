class Solution(object):
    def subarraysDivByK(self, nums, k):
        mapp = defaultdict(int)
        mapp[0] = 1
        summ, count = 0, 0

        for num in nums:
            summ += num
            div = summ % k
            count += mapp[div]
            mapp[div] += 1

        return count
