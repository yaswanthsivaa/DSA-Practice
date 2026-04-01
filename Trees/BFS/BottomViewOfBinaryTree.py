# Bottom View of the Binary Tree (Geeks for Geeks)
   # Time Complexity = O(N) + O(N log N) = O(N log N)
   # Space Complexity = O(N)

'''
class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None
'''

class Solution:
    def bottomView(self, root):
        # code here
        
        if not root:
            return []
        
        ans = []
        queue = [(0, root)]
        colValls = {}
        
        while queue:
            col, node = queue.pop(0)
            colValls[col] = node.data
            
            if node.left:
                queue.append((col-1, node.left))
            
            if node.right:
                queue.append((col+1, node.right))
            
        for key in sorted(colValls.keys()):
            ans.append(colValls[key])
        return ans
            
