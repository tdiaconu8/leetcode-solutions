class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:

        m, n = len(grid), len(grid[0])

        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return 0

        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[0][0] = 1

        for i in range(1, n):
            if grid[0][i] == 0 and dp[0][i-1]:
                dp[0][i] = 1
        for i in range(1, m):
            if grid[i][0] == 0 and dp[i-1][0]:
                dp[i][0] = 1

        for i in range(1, m):
            for j in range(1, n):
                if grid[i][j] == 0:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        return dp[-1][-1]