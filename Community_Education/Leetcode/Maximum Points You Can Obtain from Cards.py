class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        leftSum = 0
        for left in range(k):
            leftSum += cardPoints[left]
        rightSum = 0
        right = n - 1
        maxSum = leftSum + rightSum  
        for i in range(k - 1, -1, -1): 
            leftSum -= cardPoints[i]
            rightSum += cardPoints[right]
            right -= 1
            maxSum = max(maxSum, leftSum + rightSum)
        return maxSum
