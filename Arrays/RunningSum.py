# Running sum Problem (Leetcode 1480)
     # Time Complexity = O(n)
     # Space Complexity = O(n)

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        arr = [ ]      
        total =0
        for i in nums:
            total = total+i
            arr.append(total)
        return arr        
