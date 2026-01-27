# Sum of Subarray minimums
    # Time Complexity = O(N)
    # Space Complexity = O(N)

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
      def findNse(a):
            stack = []
            nse = [len(a)] * len(a)
            for i in range(len(a)-1, -1, -1):
                while stack and a[stack[-1]] >= a[i]:
                    stack.pop()
                
                if stack:
                    nse[i] = stack[-1]
                stack.append(i)
            return nse
                
        
        def findPse(a):
            stack = []
            pse = [-1] * len(a)

            for i in range(len(a)):
                
                while stack and a[stack[-1]] > a[i]:
                    stack.pop()
                
                if stack:
                    pse[i] = stack[-1]
                
                stack.append(i)
            return pse
        
        nse = findNse(arr)
        pse = findPse(arr)
        total = 0
        mod = 10**9 + 7

        for i in range(len(arr)):
            left = i - pse[i]
            right = nse[i] - i
            total += (left * right * arr[i])

        return total % mod
