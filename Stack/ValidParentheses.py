# Valid Parentheses
  # Time Complexity = O(N)
  # Space Complexity = O(N)

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
       
        for i in s:
     
            if i == "(" or i == "[" or i == "{":
                stack.append(i)
            else:
                if not stack:
                    return False
                    
                topBracket = stack[-1]
                if i == ")" and topBracket == "(":
                    stack.pop()
                elif i == "]" and topBracket == "[":
                    stack.pop()
                elif i == "}" and topBracket == "{":
                    stack.pop()
                else:
                    return False
        return stack == []
