# Majority Element in the Array 
# Time complexity : O(n)


ele = [2,2,1,1,0,3,5,1,1,0,1,1]

majority = None
count = 0

for e in ele:

  if count == 0:
    majority = e
    count = 1
  elif majority == e:
    count = count + 1
  else:
    count = count - 1

if ele.count(majority) >= len(ele) // 2:
   print(majority)
