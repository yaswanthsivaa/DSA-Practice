# Number of Sub-arrays of Size k
  # return the number of sub-arrays of size k and whose average is greater than or equal to threshold.

# Time Complexity = O(N)
# Space Complexity = O(1)


class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        
        possibleWindows = 0
        windowSum = sum(arr[:k])

        if windowSum >= threshold * k:
            possibleWindows += 1
            
        for i in range(k, len(arr)):
            windowSum += arr[i]
            windowSum -= arr[i - k]

            if windowSum >= threshold * k:
                possibleWindows += 1
        return possibleWindows


            

                
