# Fibnoccai series (Space Optimized - Version)
  # Time complexity= O(N)
  # Space complexity= O(1)


class Solution:
    def fib(self, n: int) -> int:

        if n == 0:
            return 0
        
        if n == 1:
            return 1
        
        prevPrev = 0
        prev = 1

        for i in range(2, n+1):
            curr = prev + prevPrev
            prevPrev = prev
            prev = curr
        
        return prev
