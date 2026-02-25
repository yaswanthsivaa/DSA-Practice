# Integer to Roman (Leetcode 12)

# Time Complexity = O(1)
# Space Complexity = O(1)

class Solution:
    def intToRoman(self, num: int) -> str:
        mp = {1000:'M',900:'CM', 500:'D', 400:'CD', 100:'C', 90:'XC', 50:'L', 40:'XL', 10:'X', 9:'IX', 5:'V', 4:'IV', 1:'I'}
        keys = sorted(mp.keys(), reverse=True)
        res = []

        for k in keys:
            while num >= k:
                num = num - k
                res.append(mp[k])
        
        return "".join(res)
