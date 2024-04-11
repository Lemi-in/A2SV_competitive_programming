class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        n = len(s)
        m = len(spaces)
        spaces.sort()
        added = ""
        j = 0
        for i in range(n):
            if j < m and i == spaces[j]:
                    added += ' '
                    j += 1
            added += s[i]
        while j < m:
            added += ' '
            j += 1

        return added
