# Number of Segments in a String (Leetcode 434)
  # Time Complexity = O(N)
  # Space Complexity = O(N)

class Solution:
    def countSegments(self, s: str) -> int:
        if s == "":
          return 0
    
        words = s.split()
        count = 0

        for i in words:
            if i != " ":
                count += 1
        
        return count
