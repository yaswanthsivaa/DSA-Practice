# Least Common Ancestor Problem (Leetcode 236)
   # Time Complexity = O(N)
   # Space Complexity = O(H)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def dfs(root, p, q):
           
            if not root: return None
               
            if root == p or root == q:
                return root
            
            left = dfs(root.left, p, q)
            right = dfs(root.right, p, q)
            
            if left and right:
                return root
            
            return left if left else right
            
        ans = dfs(root, p, q)
        return ans
