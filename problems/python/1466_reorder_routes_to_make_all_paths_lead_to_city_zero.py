from collections import defaultdict

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:

        graph, graphDir = defaultdict(list), defaultdict(set)
        for a, b in connections:
            graph[a].append(b)
            graph[b].append(a)
            graphDir[a].add(b)

        res = 0

        def dfs(node):
            if node in vis:
                return
            vis.add(node)
            for neigh in graph[node]:
                if neigh not in vis and node not in graphDir[neigh]:
                    nonlocal res
                    res += 1
                dfs(neigh)
            return
        
        vis = set()
        dfs(0)
        
        return res

        # T: O(E+V)
        # S: O(E+V)
