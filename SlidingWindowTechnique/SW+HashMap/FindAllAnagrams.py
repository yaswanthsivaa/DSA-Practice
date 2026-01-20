# Find All Anagrams (LC 438)
  # Time Complexity = O(n)
  # Space Complexity = O(1)

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:    
        if len(p) > len(s):
           return []

        pc = {}
        for i in p:
            pc[i] = pc.get(i, 0) + 1
        
        sc = {}
        for i in range(len(p)):
            sc[s[i]] = sc.get(s[i], 0) + 1
    
        ans = []
        if pc == sc:
           ans.append(0)
        
        left = 0
        right = len(p)
    
        for right in range(right, len(s)):
            sc[s[right]] = sc.get(s[right], 0) + 1
            sc[s[left]] = sc[s[left]] - 1
    
            if sc[s[left]] == 0:
                del sc[s[left]]
    
            left += 1
            if pc == sc:
                ans.append(left)
    
        return ans
