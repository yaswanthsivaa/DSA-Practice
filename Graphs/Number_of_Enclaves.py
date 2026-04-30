# Number_of_Enclaves (Leetcode 1020)

from collections import deque
class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        # BFS
      
        # Time Complexity = O(M x N)
        # Space Complexity = O(M x N)
      
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

        # Dfs 
      
        # Time Complexity = O(M x N)  : every cell is visited at most once
        # Space Complexity = O(M x N) : recursion stack can go up to all cells in worst case
      
        rows = len(grid)
        cols = len(grid[0])

        def dfs(i, j):

            if 0 <= i < rows and 0 <= j < cols and grid[i][j] == 1:
               grid[i][j] = "D"
            else:
                return

            dfs(i+0, j+1)
            dfs(i+0, j-1)
            dfs(i-1, j+0)
            dfs(i+1, j+0)

        for i in range(rows):
            for j in range(cols):

                if (i == 0 or i == rows-1 or j == 0 or j == cols-1) and grid[i][j] == 1:
                    dfs(i, j)
        
        
        count = 0
        for i in range(rows):
            for j in range(cols):

                if grid[i][j] == "D":
                    grid[i][j] = 1
                

                elif grid[i][j] == 1:
                    count += 1
        
        return count

