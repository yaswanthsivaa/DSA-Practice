# Count Nodes In Complete Binary Ttree (Leetcode 222)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:

        # First Way
        # Time Complexity = O(N)
        # Space Complexity = O(H)

        count = 0
        def countNode(node):
            nonlocal count
            if not node:
                return
            
            count = count + 1
            countNode(node.left)
            countNode(node.right)

        countNode(root)

        return count

        # Second Way
        # Time Complexity = O(N)
        # Space Complexity = O(H)

        def countNode(node):

            if not node:
                return 0
            
            left = countNode(node.left)
            right = countNode(node.right)

            return left + right + 1
        
        return countNode(root)



