from typing import List

class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:

        m, n = len(grid), len(grid[0])
        res = [-1] * n

        for i in range(n):
            c = i
            for r in range(m):
                newC = c + grid[r][c]
                if not (0 <= newC < n and grid[r][c] == grid[r][newC]):
                    c = -1
                    break
                c = newC
            res[i] = c

        return res