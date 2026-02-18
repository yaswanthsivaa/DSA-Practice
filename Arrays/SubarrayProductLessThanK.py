# Subarray Product Less Than K Problem (Leetcode 713)

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:

        count = 0
        n = len(nums)

        # Brute Force Solution
      
        for i in range(n):
            p = 1
            for j in range(i, n):
                res = nums[j]*p
                if res < k:
                    p = res
                    count += 1
                else:
                    break
        
        return count

        # Optimal Solution

        p = 1
        left = 0

        for right in range(n):
            p *= nums[right]
            
            while left <= right and p >= k:
                p = p // nums[left]
                left += 1

            count = count + (right - left + 1)
        return count

            

                
