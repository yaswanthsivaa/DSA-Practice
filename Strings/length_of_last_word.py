# Length of Last word in String (Leetcode 58)
   # Time Complexity = O(n)
   # Space Complexity = O(n)

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        return len(s.split(" ")[-1])
