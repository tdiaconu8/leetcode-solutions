from collections import defaultdict
from heapq import *

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:

        # T: O(m + nlog(n))
        # S: O(n+m)

        m = len(edges)
        graph = defaultdict(list)

        # Build the graph
        for i in range(m):
            a, b = edges[i]
            prob = succProb[i]
            graph[a].append((b, prob))
            graph[b].append((a, prob))

        # DIJKSTRA
        probs = [float("inf")] * n
        probs[start] = -1
        vis = set()

        pq = [(-1, start)] # priority queue
        heapify(pq)

        while pq:
            currProb, node = heappop(pq)
            vis.add(node)
            probs[node] = min(probs[node], currProb)
            for neigh, prob in graph[node]:
                if neigh not in vis:
                    heappush(pq, (currProb*prob, neigh))
        
        return 0 if probs[end] == float("inf") else -probs[end]