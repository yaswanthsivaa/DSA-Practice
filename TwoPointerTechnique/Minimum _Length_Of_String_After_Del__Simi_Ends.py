# Minimum _Length_Of_String_After_Deleting__Similar_Ends (Leetcode 1750)
  # Time Complexity = O(N)
  # Space Complexity = O(1)

class Solution:
    def minimumLength(self, s: str) -> int:
        left = 0
        right = len(s)-1

        while left < right:
            
            cp = s[left]
            cs = s[right]
        
            if cp != cs:
                break

            while left <= right and s[left] == cs:
                left += 1
               
            while left <= right and cp == s[right]:
                right -= 1
            
        return right - left + 1
            

