from collections import defaultdict
from typing import List


def gameOfLife(self, board: List[List[int]]) -> None:
    
    m, n = len(board), len(board[0])
    
    if m*n == 1:
        board[0][0] = 0
    
    neigh = defaultdict(int)
    
    # HashMap for counting number of live neighbors for each cell
    for i in range(m):
        for j in range(n):
            if i>0 and board[i-1][j] == 1:
                neigh[i*n+j] += 1
            if i<m-1 and board[i+1][j] == 1:
                neigh[i*n+j] += 1
            if i>0 and j>0 and board[i-1][j-1] == 1:
                neigh[i*n+j] += 1
            if i>0 and j<n-1 and board[i-1][j+1] == 1:
                neigh[i*n+j] += 1
            if i<m-1 and j>0 and board[i+1][j-1] == 1:
                neigh[i*n+j] += 1
            if i<m-1 and j<n-1 and board[i+1][j+1] == 1:
                neigh[i*n+j] += 1
            if j>0 and board[i][j-1] == 1:
                neigh[i*n+j] += 1
            if j<n-1 and board[i][j+1] == 1:
                neigh[i*n+j] += 1
    
    print(neigh)
    # Replace each cell with correct value
    
    for i in range(m):
        for j in range(n):
            liveN = neigh[i*n+j]
            print(liveN)
            if board[i][j] == 0:
                if liveN == 3:
                    board[i][j] = 1
            elif board[i][j] == 1:
                if liveN <= 1 or liveN > 3:
                    board[i][j] = 0
                    
    '''
    Time : O(m*n)
    Space : O(m*n)
    '''