class Solution(object):
    def simplifyPath(self, path):
        stack = []
        currSeg = ""
        for char in path + "/":
            if char == "/":
                if currSeg == "..":
                    if stack:
                        stack.pop()
                elif currSeg and currSeg != ".":
                    stack.append(currSeg)
                currSeg = ""
            else:
                currSeg += char

        return '/' + "/".join(stack)
