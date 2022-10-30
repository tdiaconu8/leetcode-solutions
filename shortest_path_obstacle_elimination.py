from heapq import *
from typing import List

class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:

        m, n = len(grid), len(grid[0])
        dirs = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        h = [(0, 0, 0, 0)] # heap queue structure : dist, i, j, obstacles
        heapify(h)
        vis = set()
        while h:
            dist, i, j, obs = heappop(h)
            if (i, j, obs) in vis or obs > k:
                continue
            if i == m-1 and j == n-1:
                return dist
            vis.add((i, j, obs))
            for di, dj in dirs:
                if 0 <= i+di < m and 0 <= j+dj < n:
                    newObs = obs + grid[i+di][j+dj]
                    heappush(h, (dist+1, i+di, j+dj, newObs))
        
        return -1