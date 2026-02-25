# Roman Number to Integer (Leetcode 13)
# Time Complexity = O(n)
# Space Complexity = O(1)

class Solution:
    def romanToInt(self, s: str) -> int:
        mp = {
            'I': 1,
            'IV':4,
            'V':5,
            'IX':9,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }

        number = 0

        for i in range(len(s)-1):
            if mp[s[i]] < mp[s[i+1]]:
                number = number - mp[s[i]]
            else:
                number = number + mp[s[i]]
        
        number += mp[s[-1]]
        return number

