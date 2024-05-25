class Solution(object):
    def characterReplacement(self, s, k):
        windowStart = 0
        maxLength = 0
        maxCount = 0
        charFrequencyMap = {}
        for windowEnd in range(len(s)):
            rightChar = s[windowEnd]
            if rightChar in charFrequencyMap:
                charFrequencyMap[rightChar] += 1
            else:
                charFrequencyMap[rightChar] = 1

            maxCount = max(maxCount, charFrequencyMap[rightChar])
            
            if (windowEnd - windowStart + 1 - maxCount) > k:

                leftChar = s[windowStart]
                charFrequencyMap[leftChar] -= 1
                windowStart += 1

            maxLength = max(maxLength, windowEnd - windowStart + 1)

        return maxLength
