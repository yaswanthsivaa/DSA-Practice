# Optimal Solution for finding the Missing Number

a = [1,2,3,5]

sum = max(a) * (max(a) + 1) / 2

sum2 = 0

for i in a:

  sum2 = sum2 + i

print(f"The Missing Number is :{sum - sum2}")

