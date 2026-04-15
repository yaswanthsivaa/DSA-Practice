# Binary SubArrays With Sum (Leetcode 930)
   # Time Complexity = O(N)
   # Space Complexity = O(1)

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:

        def atmost(goal):

            if goal < 0:
                return 0
                
            left = 0
            tot = 0
            res = 0

            for right in range(len(nums)):
                tot += nums[right]

                while tot > goal:
                    tot -= nums[left]
                    left += 1
                
                res += (right - left + 1)
            
            return res
        
        return atmost(goal) - atmost(goal-1)
        
        

   
