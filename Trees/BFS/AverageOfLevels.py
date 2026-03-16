# Average Of Levels in Binary Tree (Leetcode 637)
    # Time Complexity = O(N)
    # Space Complexity = O(N)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:

        if not root:
            return []

        result = []
        queue = [root]

        while queue:
            tot = 0
            level_size = len(queue)
            size = level_size
            
            for _ in range(level_size):
                node = queue.pop(0)
                tot += node.val

                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)
                
            avg = tot / size
            result.append(avg)
            
        return result
