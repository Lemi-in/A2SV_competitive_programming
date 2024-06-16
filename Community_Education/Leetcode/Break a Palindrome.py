class Solution(object):
    def breakPalindrome(self, s):
        p = list(s)
        if len(p) == 1: return ""
        found = -1
        for i in range(len(p)):
            if p[i] != "a" and i != len(p) // 2: #Make sure p[i] is not the middle element
                found = i
                break
        if found == -1: p[found] = 'b'
        else: p[found] = 'a'
        return ''.join(p)

