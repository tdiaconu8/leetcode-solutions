from collections import deque

class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:

        n = len(grid)

        # Approach: BFS starting from all the lands

        queue = deque([])
        vis = set()
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    queue.append((i,j,0))
                    vis.add((i,j))
        
        if not queue or len(queue) == n**2:
            return -1
        
        res = 0
        dirs = [[0,1], [0,-1], [1,0], [-1,0]]

        while queue:
            i, j, dist = queue.popleft()
            res = max(res, dist)
            for di, dj in dirs:
                if 0<=i+di<n and 0<=j+dj<n and grid[i+di][j+dj] == 0 and (i+di, j+dj) not in vis:
                    newDist = dist + abs(di) + abs(dj)
                    vis.add((i+di,j+dj))
                    queue.append((i+di, j+dj, newDist))
        
        return res
