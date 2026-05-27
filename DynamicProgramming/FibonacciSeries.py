dp = [-1] * 6

def fib(num, dp):
    
    if num <= 1:
        return num
    
    if dp[num] != -1:
        return dp[num]
    
    dp[num] = fib(num-1, dp) + fib(num - 2, dp)
    
    return dp[num]
    

print(fib(5, dp))
