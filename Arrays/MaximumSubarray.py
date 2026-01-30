# Subarray with largest Sum
  # Time Complexity = O(N)
  # Space Complexity = O(1)

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        maxx = float('-inf')
        tot = 0
        for i in range(len(nums)):
            tot = tot + nums[i]
            maxx = max(tot, maxx)

            if tot < 0:
                tot = 0
        
        return maxx
