from heapq import heappush, heappop
from typing import List


class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        
        if not maze:
            return False
        m, n = len(maze), len(maze[0])
        destX, destY  = destination
        dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        heap = [(0, start[0], start[1])]
        vis = set()
        
        while heap:
            dist, x, y = heappop(heap)
            
            if (x, y) in vis:
                continue
            vis.add((x, y))
            
            if x == destX and y == destY:
                return dist
                        
            for dx, dy in dirs:
                X, Y, curDist = x+dx, y+dy, dist
                while 0 <= X < m and 0 <= Y < n and maze[X][Y] == 0:
                    X += dx
                    Y += dy
                    curDist += 1
            
                X -= dx
                Y -= dy
                
                heappush(heap, (curDist, X, Y))
                
        return -1