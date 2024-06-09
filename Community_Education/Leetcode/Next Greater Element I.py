class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums1)
        m = len(nums2)
        ans = [-1] * n
        for i in range(n):
            if nums1[i] in nums2:
                k = nums2.index(nums1[i])
                while k < m - 1:
                    if nums2[k + 1] > nums1[i]:
                        ans[i] = nums2[k + 1]
                        break
                    k += 1

        return ans
