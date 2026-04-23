# Multiply Numbers (Leetcode 43)
   # Time Complexity = O(N)
   # Space Complexity = O(1)

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
      
        count = 0
        for n in num1:
            count = count * 10  + (ord(n) - ord('0'))
        
        count2 = 0
        for n in num2:
            count2 = count2 * 10 + (ord(n) - ord('0'))
        
        return str(count * count2)
   
