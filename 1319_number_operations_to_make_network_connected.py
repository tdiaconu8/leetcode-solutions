from collections import defaultdict

class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:

        if len(connections) < n-1:
            return -1

        graph = defaultdict(list)
        for a, b in connections:
            graph[a].append(b)
            graph[b].append(a)
        
        def dfs(node):
            if node in vis:
                return
            vis.add(node)
            for neigh in graph[node]:
                dfs(neigh)
            return
        
        groups = 0
        vis = set()
        for i in range(n):
            if i in vis:
                continue
            groups += 1
            dfs(i)
        
        return groups-1

        # T: O(V+E)
        # S: O(V*E)
