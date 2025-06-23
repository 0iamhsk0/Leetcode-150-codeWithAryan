'''
Name: 121. Best Time to Buy and Sell Stock
Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
'''

# Approach 1: Two pointers
def maxProfit(prices):
    bp = prices[0]
    profit = 0
    for price in prices[1:]:
        if price < bp:
            bp = price

        profit = max(profit, price - bp)

    return profit

# Test case
prices = [7,1,5,3,6,4]
print(maxProfit(prices))
