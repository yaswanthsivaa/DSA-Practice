# Longest Palindromic Substring (LC 5)
  #Time Complexity = O(n²)
  #Space Complexity = O(1)

class Solution:
    def longestPalindrome(self, s: str) -> str:

        n = len(s)
        lp = ""

        for i in range(n):
            left = i
            right = i + 1

            while left >= 0 and right < n:
                  if s[left]==s[right]:
                     sub = s[left:right+1]
                     if len(sub) > len(lp):
                        lp = sub
                  else:
                     break
                  left -= 1
                  right += 1

            left = right = i
            while left >= 0 and right < n:
                  if s[left]==s[right]:
                     sub = s[left:right+1]
                     if len(sub) > len(lp):
                        lp = sub
                  else:
                      break
                  left -= 1
                  right += 1

    return lp         
                        
            
                        