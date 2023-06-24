class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:

        n = len(prices)

        cache = {}
        # i index of the price, stock (-1 if stock empty, else 1)
        def dfs(i, stock):
            if (i, stock) in cache:
                return cache[(i, stock)]
            res = 0
            if i == n:
                return 0
            if stock == -1:
                res = max(-prices[i] + dfs(i+1, 1), dfs(i+1, -1))
            if stock == 1:
                res = max(prices[i] - fee + dfs(i+1, -1), dfs(i+1, 1))
            cache[(i, stock)] = res
            return res
        
        return dfs(0, -1)