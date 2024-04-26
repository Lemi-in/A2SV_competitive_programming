class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        t = temperatures
        n = len(t)
        ans = [0] * n
        stack = []
        for i in range(n):
            while stack and t[i] > t[stack[-1]]:
                prev = stack.pop()
                ans[prev] = i - prev
            stack.append(i)
        return ans
