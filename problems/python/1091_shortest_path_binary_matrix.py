# OPTIMAL SOLUTION: BFS

from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        if grid[0][0] == 1 or grid[-1][-1] == 1:  # edge case
            return -1

        n = len(grid)
        dirs = [[0,1], [0,-1], [1,0], [-1, 0], [1, -1], [-1, 1], [1, 1], [-1, -1]]
        queue = deque([(0, 0, 1)]) # queue structure : i, j, currentPath
        vis = set()
        vis.add((0,0))

        while queue:
            i, j, l = queue.popleft()
            if i == n-1 and j == n-1: # if we are at bottom, right, we return the current length
                return l
            for di, dj in dirs:
                if 0<=i+di<n and 0<=j+dj<n and grid[i+di][j+dj] == 0 and (i+di, j+dj) not in vis:
                    queue.append((i+di, j+dj, l+1))
                    vis.add((i+di, j+dj))
        
        return -1
      
      '''
      T: O(n^2)
      S: O(n^2)
      '''
      
      
     
    
    
    
####################################################################################################################################


# SECOND SOLUTION DIJKSTRA
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        if grid[0][0] == 1 or grid[-1][-1] == 1:  # edge case
            return -1
          
        n = len(grid)
        dirs = [[0,1], [0,-1], [1,0], [-1, 0], [1, -1], [-1, 1], [1, 1], [-1, -1]]
        heap = [(1, 0, 0)] # heap structure : curLength path, i, j
        heapify(heap)
        vis = set()
        vis.add((0,0))

        while heap:
            l, i, j = heappop(heap)
            if i == n-1 and j == n-1: # if we are at bottom, right, we return the current length
                return l
            for di, dj in dirs:
                if 0<=i+di<n and 0<=j+dj<n and grid[i+di][j+dj] == 0 and (i+di, j+dj) not in vis:
                    heappush(heap, (l+1, i+di, j+dj))
                    vis.add((i+di, j+dj))
        
        return -1
        
        '''
        T: O(n^2*logn)
        S: O(n^2)
        '''
