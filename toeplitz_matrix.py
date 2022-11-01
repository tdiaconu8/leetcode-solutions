from typing import List

class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:

        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            cur = matrix[i][0]
            r, c = i, 0
            while r < m and c < n:
                if matrix[r][c] != cur:
                    return False
                r, c = r+1, c+1
        
        for j in range(1, n):
            cur = matrix[0][j]
            r, c = 0, j
            while r < m and c < n:
                if matrix[r][c] != cur:
                    return False
                r, c = r+1, c+1

        return True