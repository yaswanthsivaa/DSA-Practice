# Max Area Of Island (Leetcode 695)
  # Time Complexity = O(M x N)
  # Space Complexity = O(M x N)

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        area = 0

        def countIsland(i, j):

            if 0 <= i < rows and 0 <= j < cols and grid[i][j] == 1:
                grid[i][j] = '#'

                total = (1+countIsland(i, j+1) + 
                        countIsland(i, j-1) +
                        countIsland(i-1, j) +
                        countIsland(i+1, j))
                
                return total
            else:
                return 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    count = countIsland(i, j)
                    area = max(area, count)
        
        return area
