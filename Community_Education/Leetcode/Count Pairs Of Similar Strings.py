
class Solution:
    def similarPairs(self, words: List[str]) -> int:
        d = {}
        count = 0
        for curr in words:
            word = ''.join(sorted(set(curr)))
            if word in d:
                count += d[word]
                d[word] += 1
            else:
                d[word] = 1
        return count
