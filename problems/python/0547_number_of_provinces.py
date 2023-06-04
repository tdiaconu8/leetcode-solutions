from collections import defaultdict

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        # T: O(E+V) = O(n²)
        # S: O(n²)

        n = len(isConnected)
        graph = defaultdict(set)

        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                if isConnected[i][j]:
                    graph[i].add(j)
                    graph[j].add(i)
        
        res = 0
        vis = set()

        def dfs(i):
            vis.add(i)
            for neigh in graph[i]:
                if neigh not in vis:
                    dfs(neigh)
            return

        for i in range(n):
            if i not in vis:
                res += 1
                dfs(i)

        return res