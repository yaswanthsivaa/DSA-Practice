# Squares of Sorted Arrays (Leetcode 977)

   # Time Complexity = O(N)
   # Space Complexity = O(1)

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums)-1     
        res = [0] * len(nums)
        pos = len(nums) - 1

        while left <= right:

            if abs(nums[left]) > abs(nums[right]):
                squaredNumber = nums[left] * nums[left]
                res[pos] = squaredNumber
                left += 1
            else:
                squaredNumber = nums[right] * nums[right]
                res[pos] = squaredNumber
                right -= 1
            pos -= 1
        return res 


