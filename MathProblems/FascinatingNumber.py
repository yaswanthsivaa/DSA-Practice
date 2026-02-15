# Checking If a Number is fascinating Number (Leetcode 2729)
    # Time Complexity = O(d)
    # Space Complexity = O(1)

class Solution:
    def isFascinating(self, n: int) -> bool:
        num = n
        first = 2 * n
        second = 3 * n

        res = str(num)+str(first)+str(second)

        if "0" in res:
            return False
        
        checkList = set()
        for i in res:
            if i in "123456789" and i in checkList:
                return False
            checkList.add(i)
        return True
        
