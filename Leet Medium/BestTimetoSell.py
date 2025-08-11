class Solution:
    def maxProfit(self, prices):
        """
        Problem:
        You can complete as many transactions as you like (buy one and sell one share of the stock multiple times). 
        You must sell the stock before you buy again.

        Approach:
        - We can make profit by summing up every increasing price difference.
        - Loop through prices, and whenever today's price > yesterday's price, add the difference to profit.

        Example:
        prices = [7,1,5,3,6,4]
        Profits from transactions:
        - Buy at 1, Sell at 5 → profit = 4
        - Buy at 3, Sell at 6 → profit = 3
        Total profit = 4 + 3 = 7

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]
        return profit