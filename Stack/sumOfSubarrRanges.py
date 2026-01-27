# Sum of Subarray Ranges (LC 2104)
    # Time Complexity = O(N)
    # Space Complexity = O(N)

class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        def findPse(n):
            
            stack = []
            pse = [-1] * len(n)

            for i in range(len(n)):

                while stack and n[stack[-1]] >= n[i]:
                    stack.pop()
                
                if stack:
                    pse[i] = stack[-1]
                
                stack.append(i)
            
            return pse
        
        def findNge(n):

            stack = []
            nge = [len(n)] * len(n)

            for i in range(len(n)-1, -1, -1):

                while stack and n[stack[-1]] < n[i]:
                    stack.pop()
                
                if stack:
                    nge[i] = stack[-1]
                
                stack.append(i)

            return nge
        
        def findPge(n):

            stack = []
            pge = [-1] * len(n)

            for i in range(len(n)):

                while stack and n[stack[-1]] <= n[i]:
                    stack.pop()
                
                if stack:
                    pge[i] = stack[-1]
                
                stack.append(i)
            return pge
        
        def findNse(n):

            stack = []
            nse = [len(n)] * len(n)

            for i in range(len(n)-1, -1, -1):

                while stack and n[stack[-1]] > n[i]:
                    stack.pop()
                
                if stack:
                    nse[i] = stack[-1]
                
                stack.append(i)
            
            return nse

        pse = findPse(nums)
        nse = findNse(nums)
        
        minSum = 0
        for i in range(len(nums)):
            
            left = i - pse[i]
            right = nse[i] - i

            contrib = nums[i] * left * right

            minSum = minSum + contrib

        
        maxSum = 0

        pge = findPge(nums)
        nge = findNge(nums)
        for i in range(len(nums)):
            left = i - pge[i]
            right = nge[i] - i
            contrib = nums[i] * left * right
            maxSum = maxSum + contrib
        
        return maxSum - minSum
            

        



