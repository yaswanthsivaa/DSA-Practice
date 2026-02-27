# Transform Array by parity (Leetcode 3467)

class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:

        # Brute Approach
        # Time Complexity = O(N)
        # Space Complexity = O(N)
        ans = [0 if i % 2 == 0 else 1 for i in nums]
        ans.sort()
        return ans


        # Optimal Approach

         # Time Complexity = O(2N)
         # Space Complexity = O(1)

        # Step convert 0 and 1
        for i in range(len(nums)):
            nums[i] = 0 if nums[i] % 2 == 0 else 1
        
        # Partitioning (move all 0s to front)

        left = 0

        for right in range(len(nums)):

            if nums[right] == 0:
                nums[left], nums[right] = nums[right], nums[left]
                left = left + 1
        
        return nums


      




        
        
