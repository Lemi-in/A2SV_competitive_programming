class Solution:
    def evalRPN(self, tokens):
        stack = []
        for i in range(len(tokens)):
            char = tokens[i]
            if char == "+":
                stack[-2] += stack[-1]
                stack.pop()
            elif char == "-":
                stack[-2] -= stack[-1]
                stack.pop()
            elif char == "*":
                stack[-2] *= stack[-1]
                stack.pop()
            elif char == "/":
                stack[-2] = int(float(stack[-2]) / stack[-1])
                stack.pop()
            else:
                stack.append(int(char))
        return stack[0]
