class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:

        res = 0
        n, m = len(grid), len(grid[0])
        visited = set()

        dirs = [(-1,0), (1,0), (0,-1), (0,1)]

        def dfs(i, j):
            # OUT OF BOUNDS or visited
            if i < 0 or j < 0 or i == n or j == m or (i,j) in visited or grid[i][j] == 0:
                return 0
            visited.add((i,j))
            count = 1
            for di, dj in dirs:
                count += dfs(i+di,j+dj)
            return count

        lands = 0 # Number of lands cells
        for i in range(n):
            for j in range(m):
                lands += grid[i][j]
                if grid[i][j] == 1 and (i,j) not in visited and ((i in [0, n-1]) or j in [0,m-1]):
                    res += dfs(i, j)
        
        return lands - res

        # T: O(n*m)
        # S: O(n*m)
