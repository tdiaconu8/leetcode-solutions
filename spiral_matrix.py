from typing import List


def generateMatrix(self, n: int) -> List[List[int]]:
    
    ans = [[0]* n for i in range(n)]
    vis, val = [], 1
    dirs = {}
    r, c = 0, 0
    
    directions = [[0,1], [1,0], [0,-1], [-1,0]]
    lookup = {0:1, 1:2, 2:3, 3:0}
    curDir = 0
    
    while val <= n*n:
        ans[r][c] = val
        val += 1
        vis.append([r,c])
        dr, dc = directions[curDir]
        if r+dr>=0 and r+dr<n and c+dc>=0 and c+dc<n and [r+dr, c+dc] not in vis:
            r += dr
            c += dc
        else:
            curDir = lookup[curDir]
            dr, dc = directions[curDir]
            r += dr
            c += dc
    
    return ans

'''
# Time : O(n**2)
# Space : O(**2)
'''