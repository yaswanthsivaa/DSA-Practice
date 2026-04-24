# Distribute Candies (Leetcode 575)
  class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:

        # Brute Force
        # Time Complexity = O(N)
        # Space Complexity = O(N)

        n = len(candyType)
        if n == 0:
            return 0
        ate = set()
        for i in candyType:
            if len(ate) == (n // 2):
                break
            ate.add(i)
        
        return len(ate)
        
        # better 
      
        # Time Complexity = O(1)
        # Space Complexity = O(N)
        s = set(candyType)
        h = len(candyType) // 2

        if len(s) == h or len(s) > h:
            return h
        elif len(s) < h:
            return len(s)
            
