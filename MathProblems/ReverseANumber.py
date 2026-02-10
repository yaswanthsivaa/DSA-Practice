# Reverse a Number (Leetcode 7)
    # Time Complexity = O(n)
    # Space Complexity = O(1)

class Solution:
    def reverse(self, x: int) -> int:
        
        if x < 0:
            sign = -1
            num = abs(x)
            res = 0


            while num > 0:

                digit = num % 10
                res = res * 10 + digit
                num //= 10
            
            if sign * res >= -2 ** 31 and sign * res <= 2 ** 31-1:
               return sign * res
            return 0
            
        else:
            num = x
            res = 0
            while num > 0:

                digit = num % 10
                res = res * 10 + digit
                num //= 10
            if res >= -2 ** 31 and res <= 2 ** 31-1:
               return res
            return 0
