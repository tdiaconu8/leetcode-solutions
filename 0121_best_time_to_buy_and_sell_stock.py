class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        n = len(prices)
        res, minPrice = 0, prices[0]

        for i in range(1, n):
            res = max(res, prices[i] - minPrice)
            minPrice = min(minPrice, prices[i])
        
        return res
        
        # T: O(n)
        # S: O(1)
