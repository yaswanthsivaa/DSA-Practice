# Sliding Window Maximum (Leetcode 239)
    # Time Complexity = O(N) * O(K + log K) 
                    # = O(N * K)
    # Space Complexity = O(N)

import bisect

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        currWindow = sorted(nums[:k])
        res = []
        res.append(currWindow[-1])
        
        left = 0
        for right in range(k, len(nums)):

            eliminate = bisect.bisect_left(currWindow, nums[left])
            currWindow.pop(eliminate)

            left = left + 1
            bisect.insort(currWindow, nums[right])

            res.append(currWindow[-1])
        
        return res
