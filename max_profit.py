from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        n = len(prices)
        if n == 1:
            return 0
        
        ans = 0
        curMin = prices[0]
        for i in range(1, n):
            curProfit = prices[i] - curMin
            if curProfit > ans:
                ans = curProfit
            curMin = min(curMin, prices[i])
        
        return ans
    
    # T : O(n)
    # S : O(1)