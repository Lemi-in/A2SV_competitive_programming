class Solution(object):
    def maxVowels(self, s, k):
        vowel = set('aeiou')
        maxVs = countV = 0
        for i in range(k):
            if s[i] in vowel:
                countV += 1
        maxVs = countV
        for w in range(k, len(s)):
            if s[w] in vowel:
                countV += 1
            if s[w - k] in vowel:
                countV -= 1
            maxVs = max(maxVs, countV)
        return maxVs
