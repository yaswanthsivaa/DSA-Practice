# Rotate Image Problem (Leetcode 48)
  # Time Complexity = O(n^2)
  # Space Complexity = O(n^2)

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        n = len(matrix)

        rotated = [[0 for _ in range(n)] for _ in range(n)]

        # Copying elements from original array to dummy array(rotated)
      
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                rotated[j][(n-1)-i] = matrix[i][j]

        # Pasting elements from dummy array to original array(matrix)
        for i in range(n):
            for j in range(n):
                matrix[i][j] = rotated[i][j]
              
