from collections import deque

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:

        # T: O(n+m)
        # S: O(n*m)

        INF = float("inf")
        m, n = len(mat), len(mat[0])
        dirs = [(0,1), (0,-1), (1,0), (-1,0)]
        res = [[INF for _ in range(n)] for _ in range(m)]

        queue = deque()

        def enque(i, j):
            queue.append((i,j))
        
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    res[i][j] = 0
                    enque(i, j)
        
        while queue:
            r, c = queue.popleft()
            for dr, dc in dirs:
                if 0 <= r+dr < m and 0 <= c+dc < n and res[r+dr][c+dc] == INF:
                    res[r+dr][c+dc] = 1 + res[r][c]
                    queue.append((r+dr, c+dc))
        
        return res