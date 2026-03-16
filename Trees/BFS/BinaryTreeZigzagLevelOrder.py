# Binary Tree Zig zag Level Order (Leetcode 103)
    # Time Complexity = O(N)
    # Space Complexity = O(N)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []
        
        result = []
        queue = [root]
        zizag = False

        while queue:
            level_size = len(queue)
            level = []

            for _ in range(level_size):
                node = queue.pop(0)
                level.append(node.val)

                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)
            
            if zigzag:
               result.append(level[::-1])
            else:
               result.append(level)
            zigzag = not zigzag
        
        return result


        
