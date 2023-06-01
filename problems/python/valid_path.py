from typing import List
from collections import deque

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:

        graph = {}

        for v1, v2 in edges:
            graph[v1] = graph.get(v1, []) + [v2]
            graph[v2] = graph.get(v2, []) + [v1]
        
        queue = deque([source])
        vis = set()

        while queue:
            node = queue.popleft()
            if node == destination:
                return True
            vis.add(node)
            for neigh in graph[node]:
                if neigh not in vis:
                    queue.append(neigh)
        
        return False