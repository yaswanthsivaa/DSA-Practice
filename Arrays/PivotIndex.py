# Find Pivot Index (Leetcode 724)
  # Time Complexity = O(N)
  # Space Complexity = O(1)

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)

        # Brute Force
      
        # for i in range(n):
        #     left = 0
        #     for l in range(left, i):
        #         left += nums[l]
            
        #     right = 0

        #     for r in range(i+1, n):
        #         right += nums[r]
            
        #     if left == right:
        #         return i
            
        # return -1

        total = sum(nums)
        left_sum = 0

        for i in range(n):
            right_sum = total - (left_sum + nums[i])    

            if left_sum == right_sum:
                return i
            
            left_sum += nums[i]
        
        return -1

                   
