# Maximum Number of Vowels in a Substring of Given Length (LC 1456)
  # Time Complexity = O(n)
  # Space Complexity = O(1)

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        size = len(s)

        count = 0
        for i in range(len(s[0:k])):
            if s[i] in vowels:
               count += 1
        
        left = 0
       
        maxCount = count
        for right in range(k, len(s)):

           if s[left] in vowels:
              count -= 1
              
           if s[right] in vowels:
              count += 1

           maxCount = max(maxCount, count)
           left += 1

        return maxCount
