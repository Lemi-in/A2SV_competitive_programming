class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        min_length = min(len(s) for s in strs)
        longest_prefix = ""
        
        for i in range(min_length):
            current_char = strs[0][i]
            all_same_char = all(s[i] == current_char for s in strs)
            
            if all_same_char:
                longest_prefix += current_char
            else:
                break
        
        return longest_prefix
