# Degree Of an Array (Leetcode 697)
  # Time Complexity = O(N)
  # Space Complexity = O(N)

class Solution:
    def findShortestSubArray(self, nums: List[int]):

        freq = {}
        first = {}
        last = {}

        for i, num in enumerate(nums):
            if num not in first:
                first[num] = i

            last[num] = i
            freq[num] = freq.get(num, 0) + 1

        degree = max(freq.values())
        ans = len(nums)

        for num in freq:
            if freq[num] == degree:
                ans = min(ans, last[num] - first[num] + 1)

        return ans
