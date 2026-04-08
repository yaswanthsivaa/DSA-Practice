# Path Sum II (Leetcode 113)
  # Time Complexity = O(N)
  # Space Complexity = O(H) + O(K)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        paths = []

        def checkPathSum(root, target, tot, path):
            nonlocal paths
            
            if not root:
                return
            
            tot += root.val
            path.append(root.val)

            if not root.left and not root.right:

                if tot == target:
                   paths.append(path[0:])
            
            checkPathSum(root.left, target, tot, path)
            checkPathSum(root.right, target, tot, path)

            path.pop()

        checkPathSum(root, targetSum, 0, [])

        return paths
      
