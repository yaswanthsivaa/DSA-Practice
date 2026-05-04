# Searcha2DMatrix (Leetcode 74)

# Time Complexity = O(log N x log M)        
# Space Complexity = O(1)

left = 0
right = len(matrix) - 1

while left <= right:

    mid = (left + right) // 2
    midLen = len(matrix[mid])

    if target >= matrix[mid][0] and target <= matrix[mid][midLen - 1]:
        low = 0
        high = midLen - 1

        while low <= high:  
            middle = (low + high) // 2
            if matrix[mid][middle] == target:
                return True
            elif matrix[mid][middle] > target:
                high = middle - 1
            else:
                low = middle + 1

        return False 

    elif target < matrix[mid][midLen - 1]:
        right = mid - 1
    else:
        left = mid + 1

return False



