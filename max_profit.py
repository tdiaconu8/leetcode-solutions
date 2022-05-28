from ast import List


def maxProfit(self, prices: List[int]) -> int:
    
    n, res = len(prices), 0
    buy = prices[0]
    
    for i in range(1,n):
        benefit = prices[i]-buy
        if benefit > res:
            res = benefit
        if prices[i] < buy:
            buy = prices[i]
    
    return res

'''
T: O(n)
S: O(1)
'''