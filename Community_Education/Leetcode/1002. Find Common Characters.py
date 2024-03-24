class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        n = len(words)
        common = Counter(words[0])
        for i in range(1,n):
            common &= Counter(words[i])
        return list(common.elements())
