#  Flood Fill Algorithm (Leetcode 733)
   # Time Complexity = O(N x M)
   # Space Complexity = O(N x M)

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        ini = image[sr][sc]

        def dfs(row, col, ini):
            if row < 0 or col < 0 or row >= len(image)
               or col >= len(image[0]) or image[row][col] == color
               or image[row][col] != ini:
                return
            
            image[row][col] = color

            dfs(row-1, col, ini)
            dfs(row+1, col, ini)
            dfs(row, col-1, ini)
            dfs(row, col+1, ini)
                            
        
        dfs(sr, sc, ini)
        
        return image
