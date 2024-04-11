
class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        count = {}
        
        for char in A[0]:
            count[char] = count.get(char, 0) + 1
        
        for char in count:
            for string in A[1:]:
                count[char] = min(count[char], string.count(char))
        
        result = []
        for char, freq in count.items():
            result.extend([char] * freq)
        
        return result
