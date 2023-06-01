from typing import List
from heapq import *

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:

        m, n = len(maze), len(maze[0])
        dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        heap = [(0, entrance[0], entrance[1])]
        heapify(heap)
        vis = set()
        res = float('inf')

        while heap:
            curPath, i, j = heappop(heap)
            if (i, j) in vis:
                continue
            if [i, j] != entrance and (i == 0 or i == m-1 or j == 0 or j == n-1):
                res = min(res, curPath)
                continue
            vis.add((i, j))
            for (di, dj) in dirs:
                if 0<=i+di<m and 0<=j+dj<n and (i+di, j+dj) not in vis and maze[i+di][j+dj] != '+':
                    heappush(heap, (curPath+1, i+di, j+dj))

        return res if res != float('inf') else -1