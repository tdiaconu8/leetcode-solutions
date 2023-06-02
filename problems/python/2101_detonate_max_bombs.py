from collections import defaultdict
from math import *

class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:

        # T: O(n*(E+V)) = O(n*(n+n**2)) = O(n**3)
        # S: O(n**2)
        
        n = len(bombs)
        graph = defaultdict(list)

        def computeDist(x1, y1, x2, y2):
            return sqrt((x2-x1)**2+(y2-y1)**2)

        # Build a graph
        for i in range(n-1):
            for j in range(1, n):
                b1, b2 = bombs[i], bombs[j]
                dist = computeDist(b1[0], b1[1], b2[0], b2[1])
                if dist <= b1[2]:
                    graph[i].append(j)
                if dist <= b2[2]:
                    graph[j].append(i)
        
        def dfs(i, vis):
            res = 1
            for neigh in graph[i]:
                if neigh not in vis:
                    vis.add(neigh)
                    res += dfs(neigh, vis)
            return res

        res = 0
        for i in range(n):
            vis = set()
            vis.add(i)
            res = max(res, dfs(i, vis))
        
        return res
        