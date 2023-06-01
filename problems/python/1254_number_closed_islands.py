class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:

        n, m = len(grid), len(grid[0])
        res = 0
        visited = set()

        def dfs(i, j):
            if i < 0 or i == n or j < 0 or j == m:
                return False
            if grid[i][j] == 1 or (i, j) in visited:
                return True
            visited.add((i,j))
            top =dfs(i-1, j) 
            bottom = dfs(i+1, j) 
            left = dfs(i, j-1) 
            right = dfs(i, j+1)
            return top and bottom and left and right
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0 and (i, j) not in visited:
                    res += 1 if dfs(i, j) else 0
        
        return res

        # T: O(n*m)
        # S: O(n*m)
