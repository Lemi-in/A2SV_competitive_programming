class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        left = maxKey = 0
        counts = {'T': 0, 'F': 0}

        for right in range(len(answerKey)):
            counts[answerKey[right]] += 1
            max_count = max(counts.values())
            
            while right - left + 1 - max_count > k:
                counts[answerKey[left]] -= 1
                left += 1

            maxKey = max(maxKey, right - left + 1)

        return maxKey
