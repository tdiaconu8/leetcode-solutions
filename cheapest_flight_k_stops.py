class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        graph = defaultdict(list)

        # Build the graph
        for a, b, c in flights:
            graph[a].append((b, c))
        
        heap = [(0, src, 0)] # queue structure: cost, city, dist
        heapify(heap)
        res = float('inf')
        dists = {}

        # Dijkstra
        while heap:
            cost, city, dist = heappop(heap) # pop the heap to get the minimal cost
            if dist > k+1 or (city in dists and dists[city] < dist):
                # if we made too many stops or we already visited the city with lower cost previously
                continue
            if city == dst:
                # if the city is the destination, we have the minimal possible cost
                return cost
            else:
                dists[city] = dist
                for c, p in graph[city]:
                    heappush(heap, (cost+p, c, dist+1))
        
        return -1
