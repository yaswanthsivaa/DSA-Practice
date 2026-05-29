# Fibonacci Series Tabulation Format 
  # Time Complexity = O(N)
  # Space Complexity = O(N)

dp = [-1] * (6)
dp[0] = 0
dp[1] = 1

for i in range(2, 6):
    dp[i] = dp[i-1] + dp[i-2]

print(dp)
