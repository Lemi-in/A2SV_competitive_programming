class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        loss={}
        for match in matches:
            winner, loser=match
            if winner not in loss: loss[winner]=0
            if loser in loss: loss[loser]+=1
            else: loss[loser]=1
        ans=[[], []]
        for i, f in loss.items():
            if f==0:
                ans[0].append(i)
            elif f==1:
                ans[1].append(i)
        
        return [sorted(ans[0]), sorted(ans[1])]
        
