# Boundary Traversal in Binary Tree (Gfg)

  # Time Complexity = O(n) + O(h) + O(h) = O(n)
  # Space Complexity = O(h)

class Solution:
    def boundaryTraversal(self, root):
        
        if not root:
            return []
        
        ans = [root.data]
        
        def isleaf(node):
            return node and not node.left and not node.right
        
        def leftBound(node):
            curr = node
            while curr:
                if not isleaf(curr):
                    ans.append(curr.data)
                
                if curr.left:
                    curr = curr.left
                else:
                    curr = curr.right
        
        def leafs(node):
            if not node:
                return
            
            if isleaf(node):
                if node != root: 
                    ans.append(node.data)
                return
            
            leafs(node.left)
            leafs(node.right)
        
        def rightBound(node):
            curr = node
            st = []
            
            while curr:
                if not isleaf(curr):
                    st.append(curr.data)
                
                if curr.right:
                    curr = curr.right
                elif curr.left:
                    curr = curr.left
                else:
                    break   
            while st:
                ans.append(st.pop())
        
        if not isleaf(root):
            leftBound(root.left)
            leafs(root)     
            rightBound(root.right)
        
        return ans
