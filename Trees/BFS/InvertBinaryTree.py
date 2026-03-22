# Invert Binary Tree (Leetcode 226)
   
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        # Brute Force 
        # Time Complexity = O(N^2) 
        # Space Complexity = O(N) + O(N)
      
        if not root:
            return None
        
        def bfs(root):
        # Brute Force
          queue = [root]
         
          while queue:
            level_size = len(queue)
            st = []

            for i in range(level_size):
                node = queue.pop(0)
                st.append(node)

                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)
                
            for node in st:
                temp = node.left
                node.left = node.right
                node.right = temp
        
          return root
        
        return bfs(root)

    # Optimal Solution
      # Time Complexity = O(N)
      # Space Complexity = O(N)
      if not root:
         return None
  
      queue = [root]
      while queue:
          node = queue.pop(0)
          node.left, node.right = node.right, node.left
          
          if node.left:
              queue.append(node.left)
          
          if node.right:
              queue.append(node.right)
      
      return root
    return bfs(root)
