# 3Sum closest (Leetcode 16)
  # Time complexity = O(n logn + n^2)
  # Space Complexity = O(1)

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        # Brute Force
        for i in range(len(nums)-2):
            for j in range(i+1, len(nums)-1):
                for k in range(j+1, len(nums)):
                    csum = (nums[i] + nums[j] + nums[k])
                    cdist = abs(csum - target)
                    if firstTime == True:
                       closest = csum
                       dist = cdist

                       firstTime = False
                    else:
                        if cdist < dist:
                            closest = csum
                            dist = cdist
        return closest

        # Better approach 

        nums.sort()
        
        closest = nums[0] + nums[1] + nums[2]
        dist = abs(closest - target)

        for i in range(len(nums)-2):
            left = i + 1
            right = len(nums) - 1
        
            while left < right:

                csum = nums[i] + nums[left] + nums[right]
                cdist = abs(csum - target)

                if cdist < dist:
                    closest = csum
                    dist = cdist

                if csum < target:
                    left += 1
                elif csum > target:
                    right -= 1
                else:
                    return target

        return closest







