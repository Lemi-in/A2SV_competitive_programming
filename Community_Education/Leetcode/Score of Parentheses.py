class Solution(object):
    def scoreOfParentheses(self, s):
        stack = []
        score , curr = 0 , 0
        for p in s:
            if p == "(":
                stack.append(0)
            else:
                temp = stack.pop()
                if temp == 0:
                    curr = 1
                else:
                    curr = temp * 2
                if not stack:
                    score += curr
                else:
                    stack[-1] += curr
        return score

