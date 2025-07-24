# Problem:
# You are given an array `prices` where prices[i] is the price of a stock on the i-th day.
# You want to maximize your profit by choosing a single day to buy and a different day in the future to sell.
# Return the maximum profit you can achieve. If no profit is possible, return 0.

# Approach:
# - Track the minimum price seen so far while iterating.
# - At each step, calculate profit if we sold at the current price.
# - Update the max profit if the current profit is higher.

# Time Complexity: O(n) — Single pass through the list.
# Space Complexity: O(1) — Only uses two variables.

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price  # Found a new minimum price
            elif price - min_price > max_profit:
                max_profit = price - min_price  # Found a better profit

        return max_profit
# Test case
sol = Solution()
prices = [5, 6, 2, 7, 1, 4]
print(sol.maxProfit(prices))  # Output: 5