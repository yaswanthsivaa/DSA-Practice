# N-ary Tree Level Order Traversal (Leetcode 429)
    # Time Complexity = O(N)
    # Space Complexity = O(N)

"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        from collections import deque as d
        res = []
        if not root:
            return res
        
        queue = d([root])
        while queue:
            level = []

            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                
                for child in node.children:
                    if child:
                       queue.append(child)              
            
            res.append(level)
        return res
        
