class Solution(object):
    def smallestNumber(self, num):
        if num == 0:
            return 0
        n = str(num)
        s = list(n)  
        i = 0
        if num > 0:
            s = sorted([int(i) for i in s if i.isdigit()])
            for i in range(len(s)):
                if s[i] > 0 and s[0] == 0:
                    s[i], s[0] = s[0] , s[i]
                    break
            s = [str(i) for i in s]
            s = ''.join(s)
            s = int(s)
        elif num < 0:
            s = sorted([int(i) for i in s if i.isdigit()] , reverse=True)
            s = [str(i) for i in s]
            s = ''.join(s)
            s = int(s)
            s = -1 * s
        return s
