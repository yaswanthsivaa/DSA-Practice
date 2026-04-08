# Sort Even and Odd Indices (leetcode 2164)
  # Time Complexity = O(N) + O(N logn) = O(N logn)
  # Space Complexity = O(N)

class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:

          from collections import deque

          odd = deque([])
          even = deque([])

          for i in range(len(nums)):
            if i % 2 == 0:
                even.append(nums[i])
            else:
                odd.append(nums[i])
          result = []
          
          odd = list(odd)
          even = list(even)

          odd.sort(reverse=True)
          even.sort()

          odd = deque(odd)
          even = deque(even)
          
          evenFlag = True
          for i in range(len(nums)):
            if evenFlag:
                result.append(even.popleft())
                evenFlag = False
            else:
                result.append(odd.popleft())
                evenFlag = True
          
          return result
          


