# Maximum Points You can Obtain from Cards (Leetcode 1423)
   # Time Complexity = O(2 x N)
   # Space Complexity = O(1)

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        leftSum = 0
        rightSum = 0
        maxSum = 0

        for i in range(k):
            leftSum = leftSum + cardPoints[i]
        
        maxSum = leftSum
        rightIndex = len(cardPoints)-1
      
        for j in range(k-1, -1, -1):
            leftSum -= cardPoints[j]
            rightSum += cardPoints[rightIndex]
            rightIndex -= 1

            maxSum = max(leftSum + rightSum, maxSum)
        
        return maxSum
