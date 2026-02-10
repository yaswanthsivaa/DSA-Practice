# Substrings Of Size Three with Distinct Characters (Leetcode 1876)

   # Technique used (Sliding Window + Hashmap)
   # Time Complexity = O(n)
   # Space Complexity = O(1)
  
class Solution:
    def countGoodSubstrings(self, s: str) -> int:

        if len(s) < 3:
            return 0
        
        
        # First Window

        count = 0
        currWin = {}

        for right in range(0,3):
            if s[right] not in currWin:
                currWin[s[right]] = 1
            else:
                currWin[s[right]] += 1
            
        if len(currWin) == 3:
            count = count + 1
                
        left = 1

        for right in range(3, len(s)):
            
            if s[right] not in currWin:
               currWin[s[right]] = 1
            else:
                currWin[s[right]] += 1
            
            if currWin[s[left-1]] > 1:
                currWin[s[left-1]] -= 1
            else:
                del currWin[s[left-1]]

            if len(currWin) == 3:
                count = count + 1
            
            left += 1
        return count
            

