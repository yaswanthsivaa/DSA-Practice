# Find the Index of the First Occurence of a string
   # Time Complexity = O(N)
   # Space Complexity = O(1)

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        if haystack == needle:
            return 0

        n=len(haystack)
        m=len(needle)

        for i in range(0, n-m+1):
            if haystack[i:i+m] == needle:
                return i
        
        return -1
