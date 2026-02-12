# Replace Elements With Greatest Element on Right
    # Time Complexity = O(n)
    # Space Complexity = O(1)

    class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:

        ans = []
        for i in range(len(arr) - 1, -1, -1):
            if i == len(arr) - 1:
               ans.append(-1)
               maxi = arr[i]
            else:
                ans.append(maxi)
                maxi = max(maxi, arr[i])

        ans.reverse()
        return ans

    

                
