class Solution(object):
    def evalRPN(self, tokens):
        stack = []
        for char in tokens:
            if char == "+":
                stack.append(stack.pop() + stack.pop())
            elif char == "-":
                left, right = stack.pop() , stack.pop()
                stack.append(right - left)
            elif char == "*":
                stack.append(stack.pop() * stack.pop())
            elif char == "/":
                left, right = (stack.pop() , stack.pop())
                stack.append(int(float(right)/ left))
            else:
                stack.append(int(char))
        return stack[0]
