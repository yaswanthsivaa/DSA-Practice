# RangeSumOfBST (Leetcode 938)
  # Time Complexity = O(N) in Worst-Case
  # Time Complexity = O(log N) in Avg-Case  because this is BST

  # Space Complexity = O(H)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        tot = 0
        
        def dfs(node):
            nonlocal tot
            if not node:
                return
            
            if node.val >= low and node.val <= high:
                tot = tot + node.val
            
            if node.val > low:            
               dfs(node.left)  
            
            if node.val < high:
               dfs(node.right)
        
        dfs(root)

        return tot
