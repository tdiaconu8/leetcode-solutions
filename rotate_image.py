from typing import List


def rotate(matrix: List[List[int]]) -> None:
    
    # Linear Space
    n = len(matrix)
    l, r = 0, n-1
    
    while l < r:
        for i in range(r-l):
            topLeft = matrix[l][l+i]
            matrix[l][l+i] = matrix[r-i][l]
            matrix[r-i][l] = matrix[r][r-i]
            matrix[r][r-i] = matrix[l+i][r] 
            matrix[l+i][r] = topLeft
        
        l+=1
        r-=1
    '''
    T: O(n²)
    S: O(1)
    '''

    '''    
    n = len(matrix)
    values = [0] * (n*n)
    
    for r in range(n):
        for c in range(n):
            newR, newC = c, (n-1)-r
            values[newR*n+newC] = matrix[r][c]
    
    for r in range(n):
        for c in range(n):
            matrix[r][c] = values[r*n+c]'''
    
    '''
    T: O(n²)
    S: O(n²)
    '''