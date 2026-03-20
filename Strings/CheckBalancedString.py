# Check Balanced String (Leetcode 3340)
  # Time Complexity = O(N)
  # Space Complexity = O(1)

class Solution:
    def isBalanced(self, num: str) -> bool:
        evenSum = 0
        oddSum = 0
    
        for i in range(len(num)):
            if i % 2 == 0:     
               evenSum += int(num[i])
            else:
               oddSum += int(num[i])

       
        return evenSum == oddSum
        
