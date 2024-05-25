class Solution(object):
    def balancedString(self, s):
        n = len(s)
        charCount = defaultdict(int)
        left = 0
        ans = n
        targetCount = n // 4
        for char in s:
            charCount[char] += 1

        for right in range(n):
            charCount[s[right]] -= 1
            print(charCount[s[right]])
            while (left < n and charCount['Q'] <= targetCount and charCount['W'] <= targetCount and
                   charCount['E'] <= targetCount and charCount['R'] <= targetCount):
                ans = min(ans, right - left + 1)
                charCount[s[left]] += 1
                left += 1

        return ans if ans != n else 0
