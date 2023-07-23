class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:

        dirs = [(-2,1), (-1,2), (1,2), (2,1), (2,-1), (1,-2), (-1,-2), (-2,-1)]

        cache = {}
        def dfs(i, j, moves):
            if (i,j,moves) in cache:
                return cache[(i,j,moves)]
            if i < 0 or i >= n or j < 0 or j >= n:
                return 0
            if moves == k:
                print(i,j,moves)
                return 1
            res = 0
            for di, dj in dirs:
                res += dfs(i+di, j+dj, moves+1)
            cache[(i,j,moves)] = res
            return res
        
        return dfs(row, column, 0)/(8**k)