# Insert into a Binary Search Tree
  # Time Complexity:
       # worst Case: O(N) [When Tree is skewed ]
       # Best Case: O(log N) [When Tree is balanced]
  # Space Complexity = O(H)

def insert(self, val):
    newNode = Node(val)
    
    if self.root is None:
        self.root = newNode
        return self.root
    
    def ins(node, new):
        
        if new.info < node.info:
            if not node.left:
                node.left = new
                return
            return ins(node.left, new)
        
        else:
            if not node.right:
                node.right = new
                return
            return ins(node.right, new)
    
    ins(self.root, newNode)
    
    return self.root
