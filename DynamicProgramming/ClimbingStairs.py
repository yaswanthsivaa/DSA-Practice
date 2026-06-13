class Solution:
    def climbStairs(self, n: int) -> int:

        # Memoization - solution
          # Time Complexity = O(N)
          # Space Complexity = O(N) + Recursion Stack O(K)

        # dp = [-1] * (n+1)
        # dp[1] = 1
        # dp[2] = 2
        
        # def helper(n, dp):

        #     if n == 1 or n == 2:
        #        return n
            
        #     if dp[n] != -1:
        #         return dp[n]
            
        #     dp[n] = helper(n-1, dp) + helper(n-2, dp)

        #     return dp[n]
        
        # return helper(n, dp)

        # Tabulation - solution
          # Time Complexity = O(N)
          # Space Complexity = O(N)

        if n == 1 or n == 2:
            return n

        dp = [-1] * (n + 1)
        dp[1] = 1
        dp[2] = 2

        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        
        return dp[n]

        


        



