class Solution:
    def pancakeSort(self, A: List[int]) -> List[int]:
        end=len(A)
        flips=[]
        while end>1:
            maxInd=A.index(end)
            if maxInd==end-1:
                end-=1
                continue
            if maxInd!=0:
                A[:maxInd+1]=reversed(A[:maxInd+1])
                flips.append(maxInd+1)
                
            A[:end]=reversed(A[:end])
            flips.append(end)
            end-=1
        return flips
