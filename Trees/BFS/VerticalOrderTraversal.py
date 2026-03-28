# Vertical Order Traversal Problem (Leetcode 987)
   # Time Complexity = O(N log N)
   # Space Complexity = O(N)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []
        
        col_map = {}
        queue = [(root, 0, 0)]   # (node, row, col)
        
        while queue:
            node, row, col = queue.pop(0)
            
            if col not in col_map:
                col_map[col] = []
            
            col_map[col].append((row, node.val))
            
            if node.left:
                queue.append((node.left, row + 1, col - 1))
            
            if node.right:
                queue.append((node.right, row + 1, col + 1))
        
        result = []
        
        for col in sorted(col_map.keys()):
            temp = sorted(col_map[col])   # sort by (row, value)
            col_values = []
            
            for row, val in temp:
                col_values.append(val)
            
            result.append(col_values)
        
        return result

                            
