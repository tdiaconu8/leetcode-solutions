from math import *

class Solution:
    def numSquares(self, n: int) -> int:
        
        dp = [float('inf')] * (n+1)
        dp[0] = 0

        for i in range(1, n+1):
            if int(sqrt(i)) == sqrt(i):
                dp[i] = 1
                continue
            for j in range(1, i):
                if j*j > i:
                    break
                dp[i] = min(dp[i], 1 + dp[i-j*j])
                '''if dp[i-j*j] < dp[i]:
                    dp[i] = 1 + dp[i-j*j]'''
        
        return dp[-1]