def bubbleSort(a):
  
  for i in range(0,len(a)-1):
    for j in range(0, len(a)-1-i):
      if a[j] > a[j+1]:
        t = a[j+1]
        a[j+1] = a[j]
        a[j] = t

ele = [37,5,2,4,8,40]

bubbleSort(ele)
print(ele)