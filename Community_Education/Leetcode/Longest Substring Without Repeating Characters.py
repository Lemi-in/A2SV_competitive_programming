class Solution(object):
    def lengthOfLongestSubstring(self, s):
        d = {}
        l = 0
        length = 0
        r = 0
        while r < len(s):
            letter = s[r]
            if letter in d and d[letter] >= l:
                l = d[letter] + 1
            else:
                length = max(length, r - l + 1)
            d[letter] = r
            r += 1
        return length
