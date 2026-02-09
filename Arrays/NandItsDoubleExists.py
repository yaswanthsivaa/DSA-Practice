# Check If N and Its Double Exists Problem (Leetcode 1346)
    # Time Complexity = O(n log n)
    # Space Complexity = O(1)

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        
        def check(arr, n):
            low = 0
            high = len(arr) - 1
            target = 2 * arr[n]

            while low <= high:
                mid = (low + high) // 2
                if arr[mid] == target:
                    return mid != n
                if arr[mid] > target:
                    high = mid - 1
                else:
                    low = mid + 1
            
            return False
        
        arr.sort()
        for i in range(len(arr)):
            ans = check(arr, i)
            if ans == True:
                return True
        
        return False
