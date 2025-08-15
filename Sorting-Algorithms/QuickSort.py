# QuickSort using python

def divideAndConquer(nums,low, high):
  
  pivot = nums[low]
  i = low + 1
  j = high

  while True:  
     while nums[i] <= pivot and i <= j:
       i += 1
     while nums[j] >= pivot and i <= j:
       j -= 1
     if i <= j:     
        temp = nums[j]
        nums[j] = nums[i]
        nums[i] = temp
     else:
       break
     
  temp = nums[low]
  nums[low] = nums[j]
  nums[j] = temp

  return j
     
def QuickSort(nums, low, high):
  
  if low < high:
    partition_index = divideAndConquer(nums, low, high)
    QuickSort(nums, low, partition_index-1)
    QuickSort(nums, partition_index+1, high)

numbers = [4,3,18,2]
QuickSort(numbers, 0, len(numbers)-1)
print(numbers)