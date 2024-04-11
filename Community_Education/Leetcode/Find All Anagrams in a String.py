class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n, m = len(s), len(p)
        if m > n:
            return []
        pC, sC = {}, {}
        for i in range(m):
            pC[p[i]] = pC.get(p[i], 0) + 1
            sC[s[i]] = sC.get(s[i], 0) + 1
        if pC == sC:
            ana = [0]
        else:
            ana = []
        j = 0
        i = m
        while i < n:
            sC[s[i]] = sC.get(s[i], 0) + 1
            sC[s[j]] -= 1
            if sC[s[j]] == 0:
                sC.pop(s[j])
            j += 1
            i += 1
            if sC == pC:
                ana.append(j)
        return ana
