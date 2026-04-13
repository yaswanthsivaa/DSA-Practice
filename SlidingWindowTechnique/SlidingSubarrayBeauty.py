# Sliding Subarray Beauty (Leetcode 2653)
   # Time Complexity = O(N.K)
   # Spacee Complexity = O(K)

import bisect

class Solution:
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        res = []

        curr_win = sorted(nums[:k])
        val = curr_win[x-1]

        res.append(val if val < 0 else 0)

        left = 0
        n = len(nums)
        for right in range(k, n):
            
            idx = bisect.bisect_left(curr_win, nums[left])
            curr_win.pop(idx)

            left += 1
            bisect.insort(curr_win, nums[right])

            val = curr_win[x-1]
            res.append(val if val < 0 else 0)
              
        return res
  
