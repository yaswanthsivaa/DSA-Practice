# Finding the Bottom Left Tree Value (Leetcode 513)
   # Time Complexity = O(N)
   # Space Complexity = O(N)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        if not root:
            return None
        
        queue = [root]
        ans = root.val

        while queue:
            node = queue.pop(0)
            ans = node.val

            if node.right:
                queue.append(node.right)
            
            if node.left:
                queue.append(node.left)
            
        return ans
