# Transpose Matrix (Leetcode 867)

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:

        # brute 
        # Tc : O(N^2)
        # SC : O(N^2)
        
        n = len(matrix)
        rows = len(matrix)
        cols = len(matrix[0])
        
        ans = [[0]*rows for _ in range(cols)]
        for i in range(rows):
            for j in range(cols):
                ans[j][i]=matrix[i][j]

        return ans