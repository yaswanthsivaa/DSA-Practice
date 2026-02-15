# Search a 2D Matrix (Leetcode 74)
    # Time Complexity = O(log m + log n)
    # Space Complexity = O(1)


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
      
        # Brute Force Approach
        rowLen = len(matrix)
        for i in range(rowLen):
            colLen = len(matrix[i])
            for j in range(colLen):
                if matrix[i][j] == target:
                    return True
        return False

        # Optimal Approach
      
        left = 0
        right = len(matrix) - 1

        while left <= right:

            mid = (left + right) // 2
            midLen = len(matrix[mid])

            if target >= matrix[mid][0] and target <= matrix[mid][midLen - 1]:
                low = 0
                high = midLen - 1

                while low <= high:  
                    middle = (low + high) // 2
                    if matrix[mid][middle] == target:
                        return True
                    elif matrix[mid][middle] > target:
                        high = middle - 1
                    else:
                        low = middle + 1

                return False 
            elif target < matrix[mid][midLen - 1]:
                right = mid - 1
            else:
                left = mid + 1
        
        return False
