# Book Allocation Problem (Google Asked)
# Time Complexity = O(N x sum(nums) - max(nums))
# Space Complexity = O(1)

def findPages(nums, pages):
  students = 1
  pagesCount = 0

  for i in nums:
    if i + pagesCount <= pages:
      pagesCount = pagesCount + i
    else:
      students += 1
      pagesCount = i
  
  return students


nums = list(map(int,input('Enter the Nums with space separated :').split(" ")))

k = int(input('Enter number of Students :'))

low = max(nums)
high = sum(nums)

# Brute Force 

# for i in range(low, high):
#   if findPages(nums, i) == k:
#     print(i)
#     break
  
# Optimal

answer = high
while low <= high:
    mid = (low + high) // 2

    if findPages(nums, mid) <= k:
        answer = mid
        high = mid - 1   
    else:
        low = mid + 1   

print("Minimum maximum pages:", answer)
