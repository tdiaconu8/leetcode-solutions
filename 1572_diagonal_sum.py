class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:

        n = len(mat)

        res = 0
        l, r = 0, n-1

        for i in range(n):
            if l == r:
                res += mat[i][l]
            else:
                res += mat[i][l] + mat[i][r]
            l += 1
            r -= 1
        
        return res

        # T: O(n)
        # S: O(1)
