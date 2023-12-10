# Problem 121: Best Time to Buy and Sell Stock
# Solution Runtime: 788ms (beats 94.1%)

from typing import List

def maxProfit(prices: List[int]) -> int:
    left = 0
    max_profit = 0
    for i in range(1, len(prices)):
        curr_profit = prices[i] - prices[left]
        if curr_profit < 0:
            left = i
        elif curr_profit > max_profit:
            max_profit = curr_profit
            
    return max_profit