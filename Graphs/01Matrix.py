# 01 Matrix (Leetcode 542)
  # Time Complexity = O(m x n)
  # Space Complexity = O(m x n)

from collections import deque

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows, cols = len(mat), len(mat[0])
        queue = deque()
        dist = [[-1]*cols for _ in range(rows)]
        
        # step1 : push all 0s
        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 0:
                    queue.append((i, j))
                    dist[i][j] = 0
        

        directions = [(0,1), (0,-1), (-1, 0), (1, 0)]
        # step2 : BFS
        while queue:
            r,c = queue.popleft()

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < rows and 0 <= nc < cols and dist[nr][nc] == -1:
                    dist[nr][nc] = dist[r][c] + 1
                    queue.append(((nr, nc)))
        
        return dist


