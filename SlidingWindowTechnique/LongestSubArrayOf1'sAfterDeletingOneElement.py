class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        
        longest = 0
        length = 0
        left = 0
        n = len(nums)
        zero = 0

        for right in range(n):

            if nums[right] == 0:
                zero += 1
 
            length += 1

            while zero > 1:
                if nums[left] == 0:
                    zero -= 1
                left = left + 1
                length -= 1
               
            longest = max(longest, length-1)
        
        return longest

       
