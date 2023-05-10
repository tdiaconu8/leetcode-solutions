class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:

        res = [[0 for _ in range(n)] for _ in range(n)]

        r1, r2, c1, c2 = 0, n, 0, n
        val = 1

        while val <= n**2:
            for i in range(c1, c2):
                res[r1][i] = val
                val += 1
            r1 += 1
            for i in range(r1, r2):
                res[i][c2-1] = val
                val += 1
            c2 -= 1
            for i in range(c2-1, c1-1, -1):
                res[r2-1][i] = val
                val += 1
            r2 -= 1
            for i in range(r2-1, r1-1, -1):
                res[i][c1] = val
                val += 1
            c1 += 1
        
        return res

        # T: O(n^2)
        # S: O(n^2)
