# Infix to Postfix Conversion
  # Time Complexity = O(N)
  # Space Complexity = O(N)

stack = []
s = "(p+q)*(m-n)"
postfix = ""

# Output = pq+mn-*

def priority(i):
    if i == '+' or i == '-':
        return 1
    elif i == '*' or i == '/':
        return 2
    elif i == '^':
        return 3
    else:
        return 0
    
for i in s:
    
    # If i is a operator
    if ord(i) >= ord('A') and ord(i) <= ord('Z') or ord(i) >= ord('a') and ord(i) <= ord('z') or ord(i) >= ord('1') and ord(i) <= ord('9'):
        postfix += i
    elif i == "(":
        stack.append(i)
    elif i == ")":
        while stack and stack[-1] != '(':
            postfix += stack.pop()
        stack.pop()
    else:
        while stack and priority(stack[-1]) >= priority(i):
            postfix = postfix + stack.pop()
        stack.append(i)

while stack:
    postfix = postfix + stack.pop()

print(postfix)

            
        
        
