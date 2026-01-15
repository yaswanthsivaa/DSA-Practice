# Maximum Average Subarray
   # This Problems tells Which Sub Array has the Maximum Average Comparing to other Sub arrays

# Time Complexity = O(N)
# Space Complexity = O(1)

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        windowSum = sum(nums[:k])

        maxSum = windowSum

        for i in range(k, len(nums)):
            windowSum = windowSum + nums[i]
            windowSum = windowSum - nums[i - k]
            maxSum = max(maxSum, windowSum)
        
        return maxSum / k
