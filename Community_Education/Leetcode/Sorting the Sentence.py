class Solution(object):
    def sortSentence(self, s):
        arr = s.split(' ')
        
        arr.sort(key=lambda w: int(w[-1]))  
        arr = [word[:-1] for word in arr]
        ans = ' '.join(arr)
        
        return ans
