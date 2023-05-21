from collections import deque

class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
      
        # T: O(E+V)
        # S: O(E+V)

        n = len(grid)
        dirs = [(0,1), (0,-1), (1,0), (-1,0)]
        island = set()

        # DFS to find all 1 of a same island
        def dfs(r, c):
            island.add((r, c, 0))
            for dr, dc in dirs:
                newR, newC = r+dr, c+dc
                if 0 <=newR<n and 0<=newC<n and grid[newR][newC] == 1 and (newR, newC, 0) not in island:
                    dfs(newR,newC)
            return
        
        # BFS
        def bfs():
            res = float('inf')
            queue = deque(island)  # queue structure: row, col, current Distance to reach another 1
            while queue:
                r, c, dist = queue.popleft()
                if grid[r][c] == 1 and dist > 1:
                    res = min(res, dist-1)
                for dr, dc in dirs:
                    newR, newC = r+dr, c+dc
                    if 0 <=newR<n and 0<=newC<n and (newR, newC, 0) not in island:
                        queue.append((newR, newC, dist+1))
                        island.add((newR, newC, 0))
            return res

        
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    dfs(r, c)   # we find all 1 of the island
                    return bfs()    # with the BFS, we find the shortest bridge to the other island
