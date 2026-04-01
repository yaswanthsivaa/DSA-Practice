# Symmetric Tree (Leetcode 101)
   # Time Complexity = O(N)
   # Space Complexity = O(N)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        queue = [root]

        while queue:
            level = []

            for _ in range(len(queue)):
                node = queue.pop(0)
                level.append(node)
                if node:
                   queue.append(node.left)
                   queue.append(node.right)
                
            
            left = 0
            right = len(level)-1

            while left < right:

                if level[left] is None and level[right] is None:
                    pass
                elif level[left] is None or level[right] is None:
                    return False
                elif level[left].val != level[right].val:
                    return False
                

                left += 1
                right -= 1
        
        return True

            

                


            
