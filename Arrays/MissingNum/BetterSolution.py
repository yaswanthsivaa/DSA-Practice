# Better Solution for finding Missing Number

a = [1,2,3,5]

hash = [0] * (max(a)+1)

for i in a:
  hash[i] = 1

for i in range(1,len(hash)):
  if(hash[i] == 0):
    print(i)

