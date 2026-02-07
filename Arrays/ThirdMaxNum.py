# Third Maximum Number
    # Time Complexity = O(N)
    # Space Complexity = O(1)

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        # Optimal

        if len(nums) < 3: return max(nums)

        first = second = third = float('-inf')

        for num in nums:

            if first == num or second == num or third == num: continue

            if num > first:
                third, second, first = second, first, num
            elif num > second:
                third, second = second, num
            elif num > third:
                third = num
            
        return third if third != float('-inf') else first
