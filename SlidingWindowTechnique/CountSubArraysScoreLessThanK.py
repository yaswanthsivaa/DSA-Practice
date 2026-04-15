# Count SubArrays with Score Less Than K (Leetcode 2302)
   # Time Complexity = O(N)
   # Space Complexity = O(1)

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        res = 0

        low = 0
        high = 0
       
        tot = 0
        while high < n:

            tot += nums[high]
    
            while tot * (high - low+1) >= k:
                tot -= nums[low]
                low += 1
                            
            res += (high - low + 1)
            high += 1
        
        return res

            
            
