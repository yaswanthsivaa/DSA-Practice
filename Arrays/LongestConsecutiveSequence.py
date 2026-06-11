# Longest Consecutive Sequence (Leetcode 128)

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
           return 0

        n = len(nums)
        res = 0

        # Brute - Force
          # Time Complexity = O(N^2) 
          # Space Complexity = O(1) 
          
        # nums.sort() 

        # for i in range(n):
        #     length = 1
        #     num = nums[i]

        #     for j in range(i+1, n):

        #         if nums[j] == num:
        #             continue

        #         elif num + 1 == nums[j]:
        #             length += 1
        #             num = num + 1
                
        #         else:                
        #             break
            
        #     res = max(length, res)
        
        # return res

        # Better Solution
          # Time Complexity = O(N log N) 
          # Space Complexity = O(1) 

        # nums.sort() 

        # slow = 0
        # fast = 1
        # length = 1
        # res = 0

        # while slow < fast:

        #     if fast == n:
        #         res = max(length, res)
        #         break
            
        #     if nums[fast] == nums[slow]+1:
        #         length += 1
                
        #     elif nums[fast] == nums[slow]:
        #         pass
            
        #     else:
        #         res = max(length, res)
        #         length = 1

        #     slow += 1
        #     fast += 1
        
        # return res

        # Optimal Solution
          # Time Complexity = O(N) 
          # Space Complexity = O(N) 

        num_set = set(nums)
        
        for num in nums:

            if num - 1 not in num_set:
                
                curr = num
                length = 1
                
                while curr + 1 in num_set:
                    length += 1
                    curr += 1
            
                res = max(res, length)
        
        return res
