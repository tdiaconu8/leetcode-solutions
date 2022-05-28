from typing import List


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        
        ans = 0
        dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
        
        for elem in strs:
            ones = elem.count('1')
            zeroes = elem.count('0')
            for i in range(n, ones-1, -1):
                for j in range(m, zeroes-1, -1):
                    if i-ones >= 0 and j-zeroes >= 0:
                        dp[i][j] = max(dp[i][j], dp[i-ones][j-zeroes] + 1)
        
        return dp[n][m]

# T : O(l*n*m)