from collections import defaultdict

class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:

        # T: O(n² + m) where m = roads.length
        # S: O(m) where m = roads.length

        res = 0
        graph = defaultdict(set)

        for a, b in roads:
            graph[a].add(b)
            graph[b].add(a)
        
        for i in range(n-1):
            for j in range(i+1, n):
                currRank = len(graph[i]) + len(graph[j])
                if i in graph[j]:
                    currRank -= 1
                res = max(res, currRank)
        
        return res