class Solution:
    def shiftingLetters(self, s, shifts):
        n = len(s)
        result = ''
        cShifts = 0
        prefix = [0] * (n + 1)
        
        for start, end, shift in shifts:
            if shift == 0:
                shift = -1
            prefix[start] += shift
            prefix[end + 1] -= shift
        
        for i in range(n):
            cShifts += prefix[i]
            result += chr((ord(s[i]) - ord('a') + cShifts) % 26 + ord('a'))
        
        return result
