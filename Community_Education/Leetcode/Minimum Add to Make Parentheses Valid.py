class Solution(object):
    def minAddToMakeValid(self, s):
        stack , i = [] , 0
        while i < len(s):
            if s[i] == "(": stack.append(s[i]) 
            if s[i] == ")":
                if stack and stack[-1] == "(": stack.pop()
                else: stack.append(")")
            i += 1
        return len(stack)
