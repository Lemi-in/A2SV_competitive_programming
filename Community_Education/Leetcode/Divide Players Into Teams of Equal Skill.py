class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        n = len(skill)
        if n % 2 != 0:
            return -1  
        totChem = 0
        target = sum(skill) // (n // 2)  
        f, l = 0, n - 1 
      
        while f <= l:
            curr = skill[f] + skill[l]  
            if curr != target:
                return -1  
            totChem  += skill[f] * skill[l]  
            f += 1  
            l -= 1  
        return totChem 
