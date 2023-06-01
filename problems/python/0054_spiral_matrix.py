class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        m, n = len(matrix), len(matrix[0])  # number ROWS / COLUMNS of matrix
        r1, r2, c1, c2 = 0, m, 0, n         # boundaries
        res = []                            # output

        while r1 < r2 and c1 < c2:
            # RIGHT
            for i in range(c1, c2):
                res.append(matrix[r1][i])
            r1 += 1
            # DOWN
            for i in range(r1, r2):
                res.append(matrix[i][c2-1])
            c2 -= 1
            # LEFT
            if r1 < r2:
                for i in range(c2-1, c1-1, -1):
                    res.append(matrix[r2-1][i])
                r2 -= 1
            # UP
            if c1 < c2:
                for i in range(r2-1, r1-1, -1):
                    res.append(matrix[i][c1])
                c1 += 1
        
        return res

        # T: O(n*m)
        # S: O(n*m)
