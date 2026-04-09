# Cousins In Binary Tree (Leetcode 993)
  # Time Complexity = O(N)
  # Space Complexity = O(N)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        
        from collections import deque

        queue = deque([(None, root)])
        while queue:
            level = []
            parent_x = None
            parent_y = None

            for _ in range(len(queue)):
                parent, node = queue.popleft()

                if node.val == x:
                    parent_x = parent
                
                if node.val == y:
                    parent_y = parent
                
                if node.left:
                    queue.append((node, node.left))
                
                if node.right:
                    queue.append((node, node.right))
            
            if parent_x and parent_y:
                return not parent_x == parent_y
            elif parent_x or parent_y:
                return not parent_x != parent_y
            
            
        return False
