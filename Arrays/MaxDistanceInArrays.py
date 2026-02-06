# Maximum Distance in Arrays (Leetcode 624)
      # Time Complexity = O(N)
      # Space Complexity = O(1)

class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        mini = arrays[0][0]
        maxi = arrays[0][-1]
        
        ans = float('-inf')
        for i in range(1, len(arrays)):
            diff = abs(mini - arrays[i][-1])
            ans = max(ans, diff)

            diff = abs(arrays[i][0] - maxi)
            ans = max(ans, diff)
            
            mini = min(mini, arrays[i][0])
            maxi = max(maxi, arrays[i][-1])
        
        return ans
