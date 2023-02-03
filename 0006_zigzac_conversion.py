class Solution:
    def convert(self, s: str, numRows: int) -> str:

        if numRows == 1: return s # edge case : if numRows is 1, we return the initial string

        n, rows = len(s), numRows
        matrix = [[-1 for _ in range(n)] for _ in range(rows)] # matrix to store the result pattern

        i = 0 # iterator over the string
        pos = (0, 0, -1) # current position : row, column and direction (-1 for bottom, 1 for top)

        while i < n:
            r, c, dir = pos
            matrix[r][c] = s[i]
            if dir == -1:
                if r < rows-1:
                    r += 1
                elif r == rows-1:
                    r, c, dir = r-1, c+1, 1
            elif dir == 1:
                if r > 0:
                    r, c = r-1, c+1
                elif r == 0:
                    r, dir = r+1, -1
            i += 1
            pos = (r, c, dir)
        
        res = ''
        for i in range(rows):
            for j in range(n):
                if matrix[i][j] == -1:
                    continue
                else:
                    res += matrix[i][j]
        
        return res

        '''
        len(s) = N, numRows = M
        T: O(N*M)
        S: O(N*M)
        '''
