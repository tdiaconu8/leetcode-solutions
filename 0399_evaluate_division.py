from collections import defaultdict, deque

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        # T: O(Q*(E+V))
        # S: O(E+V)

        # Build graph
        graph = defaultdict(list)
        for i in range(len(equations)):
            a, b = equations[i]
            val = values[i]
            graph[a].append((b, val))
            graph[b].append((a, 1/val))
        
        # DFS
        def dfs(num, dest, curDiv, vis):
            if num not in graph or dest not in graph:
                return -1
            if num == dest:
                return curDiv
            vis.add(num)
            for neigh, div in graph[num]:
                if neigh not in vis:
                    tmp = dfs(neigh, dest, curDiv*div, vis)
                    if tmp != -1:
                        return tmp
            return -1

        return [dfs(a,b,1,set()) for a,b in queries]
