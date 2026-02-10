# Intersection Of Multiple Arrays (Leetcode 2248)
  # Time Complexity = : O(k · n + n log n)
  # Space Complexity = O(n)

class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        common = set(nums[0])

        for i in range(1, len(nums)):
            common = common.intersection(nums[i])
        return sorted(common)