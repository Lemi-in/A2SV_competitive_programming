class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        l, r = 0, n - 1
        ans = []
        while l < r:
            sum2 = numbers[l] + numbers[r]
            if sum2 > target:
                r -= 1
            elif sum2 < target:
                l += 1
            else:
                ans.append(l + 1)
                ans.append(r + 1)
                break  
        return ans
