class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # Brute Force Approach
        # Time Complexity = O(N^2)
        # Space Complexity = O(1)

        maxProfit = 0
        n = len(prices)
        for i in range(n):
            for j in range(i+1, n):
                currProfit = prices[j] - prices[i]
                if currProfit > maxProfit:
                    maxProfit = currProfit
        
        return maxProfit

        # better solution
        # Time Complexity = O(N)
        # Space Complexity = O(N)

        future_max = [0] * n
        future_max[n-1] = prices[n-1]
        for i in range(n-2, -1, -1):
            future_max[i] = max(prices[i], future_max[i+1])
        
        max_profit = 0

        for i in range(n):
            profit = future_max[i] - prices[i]
            max_profit = max(max_profit, profit)
        
        return max_profit

        # Optimal Approach
        # Time Complexity = O(N)
        # Space Complexity = O(1)

        min_price = float('inf')
        max_profit = 0
        for price in prices:
            if price < min_price:
                min_price = price
            else:
                profit = price - min_price
                max_profit = max(max_profit, profit)
        
        return max_profit
        


        
        
