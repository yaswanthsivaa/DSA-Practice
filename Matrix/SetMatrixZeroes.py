# Set Matrix Zeroes (Leetcode 73)
  # Time Complexity = O(N^2)
  # Space Complexity = O(N)

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        zeroPos = []
        col = len(matrix)
        row = len(matrix[0])

        for i in range(col):
            for j in range(row):
                if matrix[i][j] == 0:
                    zeroPos.append((i, j))
        
        
        for pos in zeroPos:
            i, j = pos[0], pos[1]

            for r in range(row):
                matrix[i][r] = 0
            
            for c in range(col):
                matrix[c][j] = 0
        

            


