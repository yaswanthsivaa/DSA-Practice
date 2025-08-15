# Selection Sort
# 

def selectionSort(numbers, size):
  
  for i in range(size-1):
    min_value = i
    for j in range(i+1,size):
       
       if numbers[j] < numbers[min_value]:
         min_value = j
    
    temp = numbers[min_value]
    numbers[min_value] = numbers[i]
    numbers[i] = temp

nums = [4,3,2,1]
selectionSort(nums, len(nums))
print(nums)