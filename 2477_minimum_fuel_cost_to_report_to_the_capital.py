from collections import defaultdict, deque

class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:

        graph = defaultdict(list)

        for a, b in roads:
            graph[a].append(b)
            graph[b].append(a)

        self.res = 0

        def dfs(node, par, dist): # DFS : current node, parent, current distance
            people = 1
            for neigh in graph[node]:
                if neigh != par:
                    people += dfs(neigh, node, dist+1)
            if dist > 0:
                self.res += (people-1)//seats+1
            return people
        
        dfs(0, 0, 0)
        return self.res

        # T: O(n)
        # S: O(n)
