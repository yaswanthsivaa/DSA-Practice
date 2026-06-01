# Fibnoccai series 
  # Time complexity= O(N)
  # Space complexity= O(1)

num = int(input("Enter the number for finding the fibonacci Number: "))

prev2 = 0
prev = 1

for i in range(2, num+1):
    curr_i = prev + prev2
    prev2 = prev
    prev = curr_i

print(prev)