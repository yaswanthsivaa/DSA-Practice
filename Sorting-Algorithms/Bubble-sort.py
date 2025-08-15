# BubbleSort

def bubbleSort(nums):
    size = len(nums)
  
    for i in range(size-1):
        # printing elements at Every pass
        print(nums)

        for j in range(size-1):
          
          if nums[j] > nums[j+1]: 
              t = nums[j]
              nums[j] = nums[j+1]
              nums[j+1] = t
            

numbers = [5, 1, 4, 2, 8]
print("numbers before sorted :", numbers)
bubbleSort(numbers)
print("numbers after sorted :",numbers)
