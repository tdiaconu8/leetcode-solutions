from collections import defaultdict

class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:

        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        rem = 0 # nb of unvisited nodes

        def dfs(node):
            count = 1
            for neigh in graph[node]:
                nonlocal vis
                if neigh not in vis:
                    vis.add(neigh)
                    count += dfs(neigh)
            return count
        
        res = 0
        vis = set()
        for i in range(n):
            if i not in vis:
                vis.add(i)
                group = dfs(i)
                rem += group
                res += group * (n-rem)

        return res

        # T: O(E+V)
        # S: O(E+V)
