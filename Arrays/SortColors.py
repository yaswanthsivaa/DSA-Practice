# Sort Colors (Leetcode 75)
   # Time Complexity = O(n^2)
   # Space Complexity = O(1)

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Selection Sort
        
        n = len(nums)
        for i in range(n):
            for j in range(i, n):
                if nums[j] < nums[i]:
                    temp = nums[i]
                    nums[i] = nums[j]
                    nums[j] = temp
        
        # Insertion Sort

        for i in range(1, n):
            j = i
            while j != 0 and nums[j] < nums[j-1]:
                nums[j-1], nums[j] = nums[j], nums[j-1]
                j = j - 1
            
        
        
