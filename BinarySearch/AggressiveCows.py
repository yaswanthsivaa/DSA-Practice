# Aggressive Cows Problem

# Time Complexity = O(n log n + n log(max(nums) − min(nums)))
# Space Complexity = O(1)

def canWePlace(arr, distance, cows):
    countCows = 1
    last = arr[0]
    
    for i in range(1, len(arr)):
        if arr[i] - last >= distance:
            countCows += 1
            last = arr[i]
    
    return countCows >= cows

# Brute Force

#     nums.sort() # O(n logn)
#     ans = 0
#     for i in range(1, max(nums)-min(nums)+1):
#         if self.c(nums, i, k) == True:
#             ans = i
#         else:
#             break

#     return ans

# Optimal (Binary Search)
    
nums = [0,3,4,6,10,9]
k = 4
nums.sort()
low = 1
high = max(nums) - min(nums) 

while low <= high:
    mid = (low + high) // 2
    if canWePlace(nums, mid, k) == True:
       low = mid + 1
    else:
       high = mid - 1

print(high)
            
        
                
