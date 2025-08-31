# Rotating the List by 1 element
# Time Complexity :-- O(n) & Space Complexity :-- O(1)

num = [1,2,3,4]

temp = num[0]

for i in range(1,len(num)):
    
    num[i-1] = num[i]

num[len(num)-1] = temp

print(num)