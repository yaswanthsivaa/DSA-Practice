# Missing Number

num = [1,2,3,4,5]

for i in range(1,6):
  flag = True
  for j in num:
    if j == i:
       flag = True
       break
    flag = False
    continue
  if flag == False: print(i)
    
