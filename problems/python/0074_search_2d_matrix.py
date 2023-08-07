class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        # T: O(log(m*n))
        # S: O(1)

        m, n = len(matrix), len(matrix[0])

        l, r = 0, m-1
        while l <= r:
            m = (l+r)//2
            if matrix[m][0] > target:
                r = m-1
            elif matrix[m][-1] < target:
                l = m+1
            else:   # matrix[m][0] <= target <= matrix[m][-1]
                break
            
        row = (l+r)//2

        l, r = 0, n-1
        while l <= r:
            m = (l+r)//2
            if matrix[row][m] == target:
                return True
            elif matrix[row][m] > target:
                r = m-1
            elif matrix[row][m] < target:
                l = m+1
            
        
        return False