# Max Consecutive Ones Problem (Leetcode 485)
    # Time Complexity = O(N)
    # Space Complexity = O(1)

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        currentCount = maxCount = 0

        for i in nums:
            if i == 1:
                currentCount = currentCount + 1
            else:
                maxCount = max(maxCount, currentCount)
                currentCount = 0
        
        maxCount = max(maxCount, currentCount)
        return maxCount

        
