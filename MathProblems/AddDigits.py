# Add digits (Leetcode 258)
   # Time complexity = O(log N)
   # Space Complexity = O(1)

class Solution:
    def addDigits(self, num: int) -> int:
        curr = num
        while curr >= 10:
            digit = curr % 10
            curr = curr // 10
            curr = curr + digit            
        
        return curr
