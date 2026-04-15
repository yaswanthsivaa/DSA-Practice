# Word Pattern (Leetcode 290)
  # Time Complexity = O(N^2)
  # Space Complexity = O(N)

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        pairs = {}
        words = s.split()
        
        if len(words) != len(pattern):
            return False

        for i in range(len(words)):
            
            for key in pairs:
                if pairs[key] == words[i] and key != pattern[i]:
                    return False
            
            if pattern[i] not in pairs:
               pairs[pattern[i]] = words[i]
            else:
                if pairs[pattern[i]] != words[i]:    
                   return False
                
        
        return True
