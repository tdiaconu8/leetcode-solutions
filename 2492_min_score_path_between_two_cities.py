from collections import defaultdict

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:

        graph = defaultdict(list)
        for a, b, dist in roads:
            graph[a].append((b, dist))
            graph[b].append((a, dist))

        def dfs(node):
            if node in vis:
                return
            vis.add(node)
            for neigh, dist in graph[node]:
                nonlocal res
                res = min(res, dist)
                dfs(neigh)
            
        res = float('inf')
        vis = set()
        dfs(1)
        return res
      
      # T: O(n)
      # S: O(1)
