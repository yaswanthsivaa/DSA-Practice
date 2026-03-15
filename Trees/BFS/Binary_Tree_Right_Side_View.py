# Binary Tree Right Side View (Leetcode 199)
  # Time Complexity = O(N)
  # Space Complexity = O(N)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        if not root:
            return []

        result = []
        Queue = [root]

        while Queue:
            level_size = len(Queue)

            for i in range(level_size):
                node = Queue.pop(0)
                if i == level_size - 1:
                    result.append(node.val)
                
                if node.left:
                    Queue.append(node.left)
                
                if node.right:
                    Queue.append(node.right)
            
        return result
            
                
                
