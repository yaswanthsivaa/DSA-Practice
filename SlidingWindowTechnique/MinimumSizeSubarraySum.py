# Minimum Size Subarray Sum.py (Leetcode 209)
    # Time Complexity = O(n)
    # Space Complexity = O(1)

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        minLen = float('inf')
        left = 0
        tot = 0

        for right in range(len(nums)):
            tot += nums[right]

            while tot >= target:
                windowlen = right - left + 1
                minLen = min(minLen, windowlen)
                tot = tot - nums[left]
                left = left + 1

        # If minLen is not changed that means we did not find any valid subarray whose sum is equal to target ...
        if minLen == float('inf'):
            return 0
            
        return minLen
