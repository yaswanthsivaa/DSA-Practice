# Reverse Words in a String (Leetcode 557)
    # Time Complexity = O(n)
    # Space Complexity = O(n)

class Solution:
    def reverseWords(self, s: str) -> str:
        # normal way

        words = s.split()

        res = []

        for i in words:
            rev = i[::-1]
            res.append(rev)
        
        return " ".join(res)


        



            
