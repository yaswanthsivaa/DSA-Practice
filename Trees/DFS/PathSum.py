# Path Sum Problem (Leetcode 112)
  # Time Complexity = O(N)
  # Space Complexity = O(H)

def checkPathSum(root, target, total):
            if not root:
                return False
            
            total = total + root.val
            
            if not root.left and not root.right: # heart
                if target == total:
                   return True
                else:
                    return False
            
            left = checkPathSum(root.left, target, total)
            right = checkPathSum(root.right, target, total)
             
            return left or right
        
        return checkPathSum(root, targetSum, 0)
