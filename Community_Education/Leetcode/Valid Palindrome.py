#First approach (brute force)
"""
class Solution(object):
    def isPalindrome(self, s):
        words = []
        for word in s:
            if word.islower():
                words.append(word)
            elif word.isupper():
                words.append(word.lower())
        words = ''.join(words)
        reversedWords = words[::-1]
        return words == reversedWords
"""
#Second approach
class Solution(object):
    def isPalindrome(self, s):
        left , right = 0 , len(s) - 1
        while left < right:
            if not s[left].isalnum():
                left += 1
            elif not s[right].isalnum():
                right -= 1
            elif s[left].lower() == s[right].lower():
                left += 1
                right -= 1
            else:
                return False
        return True



