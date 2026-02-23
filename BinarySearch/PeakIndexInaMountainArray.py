# Peak Index in a Mountain Array (Leetcode 852)
     # Time Complexity = O(log n)
     # Space Complexity = O(1)

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:

        # Linear Seach

        # num = arr[0]
        # for i in range(1, len(arr)-1):

        #     if arr[i] > num and arr[i] > arr[i+1]:
        #         return i
        #     num = arr[i]

        # Binary Search 

        left = 0
        right = len(arr) - 1

        while left < right:
            mid = (left + right) // 2

            if arr[mid] > arr[mid - 1] and arr[mid] > arr[mid + 1]:
                return mid
            elif arr[mid - 1] > arr[mid]:
                right = mid
            elif arr[mid + 1] > arr[mid]:
                left = mid
            
            
