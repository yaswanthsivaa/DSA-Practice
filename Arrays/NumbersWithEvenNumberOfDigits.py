# Find Numbers with Even Numbers of Digits
     
class Solution:
    def findNumbers(self, nums: List[int]) -> int:

        # First Approach

        # Time Complexity = O(N * d)
        # Space Complexity = O(d)

        count = 0
        for i in nums:
            if len(str(i)) % 2 == 0:
                count = count + 1
        
        return count

        # Second Approach

        # Time Complexity = O(N * d)
        # Space Complexity = O(1)

        tot = 0
        for i in nums:
            count = 0
            curr = i

            while curr > 0:
                curr = curr // 10
                count += 1
            
            if count % 2 == 0:
                tot += 1
        
        return tot
