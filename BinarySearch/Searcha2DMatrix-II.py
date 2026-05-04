# Searcha2DMatrix (Leetcode 240)

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        # brute force
          # Time Complexity = O(N x M)
          # Space Complexity = O(1)

        Time Complexity = O(N x M)
        Space Complexity = O(1)

        for i in matrix:
            for j in i:
                if j == target:
                    return True
        
        return False

        # better solution

          # Time Complexity = O(N x logn)
          # Space Complexity = O(1)

        def binarySearch(arr):
            low = 0
            high = len(arr)-1

            while low <= high:
                mid = (low + high) // 2
                if arr[mid] == target:
                    return True
                
                elif arr[mid] < target:
                    low = mid + 1
                
                else:
                    high = mid - 1
            
        n = len(matrix)

        for i in range(n):

            if binarySearch(matrix[i]):
                return True
        
        return False

        # optimal Solution
      
          # Time Complexity = O(N + M)
          # Space Complexity = O(1)

        row = 0
        col = len(matrix[0])-1

        while col > -1 and row < len(matrix):

            if matrix[row][col] == target:
                return True
            
            elif matrix[row][col] > target:
                col = col - 1
            
            elif matrix[row][col] < target:
                row = row + 1
        
        return False
