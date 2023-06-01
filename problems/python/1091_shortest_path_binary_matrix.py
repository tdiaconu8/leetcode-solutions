from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        # BFS
        # T: O(n²)
        # S: O(n²)

        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1

        n = len(grid)
        queue = deque([(0, 0, 1)])   # row, column, nb of visited cells
        dirs = [(0,1), (0,-1), (1,0), (-1,0), (1,1), (1,-1), (-1,1), (-1,-1)]
        vis = set()
        vis.add((0,0))

        while queue:
            r, c, dist = queue.popleft()
            if r == n-1 and c == n-1:
                return dist
            for dr, dc in dirs:
                if 0 <= r+dr < n and 0 <= c+dc < n and grid[r+dr][c+dc] == 0 and (r+dr, c+dc) not in vis:
                    queue.append((r+dr, c+dc, dist+1))
                    vis.add((r+dr, c+dc))
        
        return -1