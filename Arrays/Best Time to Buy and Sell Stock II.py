'''
Name: 122. Best Time to Buy and Sell Stock II
Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/'''

# Approach 1: Using slow and fast pointers
def maxProfit(prices):
    profit = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i-1]:
            profit += prices[i] - prices[i-1]
    
    return profit

# Test case:
prices = [7,1,5,3,6,4] # 7
print(maxProfit(prices))