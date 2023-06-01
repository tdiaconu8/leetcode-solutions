"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':

        n = len(grid)
        print(n)

        # check if the values are the same
        val, isSame = grid[0][0], True
        for i in range(n):
            for j in range(n):
                if grid[i][j] != val:
                    isSame = False
                    break
        
        if isSame:
            return Node(val, True)
        
        topLeft = self.construct([grid[i][:n//2] for i in range(n//2)])
        topRight = self.construct([grid[i][n//2:] for i in range(n//2)])
        bottomLeft = self.construct([grid[i][:n//2] for i in range(n//2,n)])
        bottomRight = self.construct([grid[i][n//2:] for i in range(n//2,n)])
        
        return Node(1, False, topLeft, topRight, bottomLeft, bottomRight)

        # T: O(n^2*log2(n))
        # S: O(n^2*log2(n))
