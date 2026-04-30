# Number_of_Enclaves (Leetcode 1020)
  # Time Complexity = O(M x N)
  # Space Complexity = O(M x N)

from collections import deque
class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        Queue = deque()

        for i in range(rows):
            for j in range(cols):

                if grid[i][j] == 1 and (i == 0 or j == 0  or i == rows-1 or j == cols-1):
                    Queue.append((i, j))
                    grid[i][j] = "D"
        
        while Queue:
            i, j = Queue.popleft()

            for dr,dc in [(0,1), (0,-1), (1,0), (-1,0)]:
                nr, nc = i + dr, j + dc

                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    grid[nr][nc] = "D"
                    Queue.append((nr, nc))
        
        count = 0
        for i in range(rows):
            for j in range(cols):

                if grid[i][j] == 1:
                    count += 1
                
                if grid[i][j] == "D":
                    grid[i][j] = 1
        
        return count

