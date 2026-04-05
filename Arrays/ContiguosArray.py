# Contiguos Array (Leetcode 525)

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        # brute Force 
          # Time Complexity = O(N^2)
          # Space Complexity = O(1)
        maxLen = 0
        n = len(nums)
        for i in range(n):

            count0 = 0
            count1 = 0

            for j in range(i, n):

                if nums[j] == 0:
                    count0 += 1
                else:
                    count1 += 1
                
                if count0 == count1:
                    maxLen = max(maxLen, j - i + 1)
                
        return maxLen

        # Optimal Solution
          # Time Complexity = O(N)
          # Space Complexity = O(N)
        prefix_sum = 0
        maxLen = 0
        mp = {0:-1}

        for i in range(len(nums)):
            if nums[i] == 0:
                prefix_sum -= 1
            else:
                prefix_sum += 1
            
            if prefix_sum in mp:
                maxLen = max(maxLen, i - mp[prefix_sum])
            else:
                mp[prefix_sum] = i
            
        return maxLen
