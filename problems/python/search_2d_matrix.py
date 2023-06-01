from typing import List


def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    
    m, n = len(matrix), len(matrix[0])
    l, r = 0, m-1
    
    while l+1 < r:
        middle = (l+r)//2
        if matrix[middle][0] > target:
            r = middle-1
        else:
            l = middle
    
    if target in matrix[l] or target in matrix[r]:
        return True
    return False

# Time : O(log(n)+log(m))
# Space : O(1)