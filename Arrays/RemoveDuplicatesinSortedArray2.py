# Remove Duplicates in a sorted Array II
    # Time Complexity = O(n)
    # Space Complexity = O(1)

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        # Brute Force

        # i = 0
        # while i < len(nums):
        #     count = 1
        #     j = i + 1
        #     while j < len(nums) and nums[j] == nums[i]:
        #        count += 1
        #        j += 1
        
        #     while count > 2:
        #         nums.pop(i + 2)
        #         count -= 1
            
        #     i += 1
        # return len(nums)

        # optimal

        if len(nums) <= 2:
           return len(nums)
        
        write = 2

        for read in range(2, len(nums)):

            if nums[read] != nums[write - 2]:
               nums[write] = nums[read]
               write += 1
        return write


