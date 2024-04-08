class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        f, l = 0, n - 1
        ope = 0

        while f < l:
            curr = nums[f] + nums[l]
            if curr == k:
                ope += 1
                f += 1
                l -= 1

            elif curr > k:
                l -= 1
            else:
                f += 1
        return ope
