from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        n = len(prices)
        
        if n < 2: # edge case : if no more than one element, the profit is 0
            return 0
        
        # we initiliaze 3 variables
        # buy : profit if last action is buy
        # sell : profit if last action is a sell
        # last_sell : profit at the last sell action
        buy, sell, last_sell = -prices[0], 0, 0 

        # at a state i
        # buy : max(last_sell-prices[i], buy)
        # sell : max(buy+prices[i], sell)
        # last sell : sell
        for i in range(1, n):
            buy, sell, last_sell = max(last_sell-prices[i], buy), max(buy+prices[i], sell), sell
        
        # we return the max between the two action
        return max(buy, sell)