class Solution(object):
    def minWindow(self, source, target):
        if target == "":
            return ""
        
        targetCount, windowCount = {}, {}
        for char in target:
            targetCount[char] = targetCount.get(char, 0) + 1
        
        have, need = 0, len(targetCount)
        result, resultLength = [-1, -1], float("inf")
        left = 0
        
        for right in range(len(source)):
            char = source[right]
            windowCount[char] = 1 + windowCount.get(char, 0)

            if char in targetCount and windowCount[char] == targetCount[char]:
                have += 1

            while have == need:
                if (right - left + 1) < resultLength:
                    result = [left, right]
                    resultLength = (right - left + 1)
                
                windowCount[source[left]] -= 1
                if source[left] in targetCount and windowCount[source[left]] < targetCount[source[left]]:
                    have -= 1
                
                left += 1
        
        left, right = result
        return source[left:right + 1] if resultLength != float("inf") else ""
