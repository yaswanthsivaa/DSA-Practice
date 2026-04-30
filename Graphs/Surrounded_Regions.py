# Surrounded Regions (Leetcode 130)
  # Time Complexity = O(M x N)
  # Space Complexity = O(M x N)

from collections import deque

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        cols = len(board[0])

        queue = deque()

        for i in range(rows):
            for j in range(cols):

                if (i == 0 or j == 0 or i == rows-1 or j == cols-1) and board[i][j] == "O":
                    queue.append((i, j))
                    board[i][j] = "S"
                

        directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        while queue:
            i, j = queue.popleft()

            for dr, dc in directions:
                nr, nc = i + dr, j + dc
                
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] == "O":
                    queue.append((nr,nc))
                    board[nr][nc] = "S"
        
        for i in range(rows):
            for j in range(cols):

                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "S":
                    board[i][j] = "O"
                

        
        
                
                

         
