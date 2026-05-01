# Word Length (Leetcode 79)
  # Time Complexity = O(M x N x 4^L) : from one cell → we try 4 side paths in worst-case
  # Space Complexity = O(L) : we store length of the path (recursion depth)


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # DFS + BACKTRACKING

        def search(i, j, index):
            if index == len(word):
                return True
            
            if 0 <= i < rows and 0 <= j < cols and board[i][j] == word[index]:
                temp = board[i][j]
                board[i][j] = '#'
            
                found = (search(i, j+1, index+1) or
                         search(i, j-1, index+1) or
                         search(i-1, j, index+1) or
                         search(i+1, j, index+1)
                        )
                
                board[i][j] = temp

                return found
            else:
                return False

        rows = len(board)
        cols = len(board[0])

        for i in range(rows):
            for j in range(cols):

                if search(i, j, 0):
                    return True
        
        return False
                    
