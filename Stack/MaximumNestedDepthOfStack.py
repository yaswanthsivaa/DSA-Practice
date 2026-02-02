#  Maximum Nesting Depth of the Parentheses
   # Time Complexity = O(N)
   # Space Complexity = O(N)


class Solution:
    def maxDepth(self, s: str) -> int:

        depth = 0
        currentDepth = 0
      
        stack = []
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(s[i])
                currentDepth = currentDepth + 1
                depth = max(depth, currentDepth)
            elif s[i] == ')':
                if stack and stack[-1] == '(':
                    stack.pop()
                    currentDepth -= 1
            
        return depth
