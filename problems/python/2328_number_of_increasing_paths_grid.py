class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:

        m, n = len(grid), len(grid[0])
        MOD = 10**9+7

        dirs = [(0,1), (0,-1), (-1,0), (1, 0)]
        # Function that returns the nb of striclty increasing paths starting from i j
        cache = {}
        def dfs(i, j):
            if (i, j) in cache:
                return cache[(i,j)]
            res = 1
            for di, dj in dirs:
                if 0 <= i+di < m and 0 <= j+dj < n and grid[i+di][j+dj]>grid[i][j]:
                    res += dfs(i+di, j+dj)
            cache[(i,j)] = res
            return res%MOD
        
        res = 0
        for i in range(m):
            for j in range(n):
                res += dfs(i,j)
        return res%MOD