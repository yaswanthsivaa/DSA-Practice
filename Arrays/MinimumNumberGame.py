# Minimum Number Game (Leetcode 2974)

    # Time Complexity = O(n logn) + O(n)
    #                 = O(n logn)  --> when analyzing Big-O we keep the dominant term
    # Space Complexity = O(n)

class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        ans=[]
        nums.sort()
        left = 0
        for right in range(1,len(nums),2):
            left = right -1
            ans.append(nums[right])
            ans.append(nums[left])

        return ans
