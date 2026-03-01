# Jewels and Stones (Leetcode 771)
    # Time Complexity = O(n)
    # Space Complexity = O(1)

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewelsHave = 0
        for i in range(len(stones)):
            if stones[i] in jewels:
                jewelsHave += 1
         
        return jewelsHave
