from heapq import *

class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:

        n, res = len(costs), 0
        
        p1, p2 = candidates-1, n-candidates
        session = []
        for i in range(p1+1):
            session.append((costs[i], 0))
        
        for i in range(max(p1+1, p2), n):
            session.append((costs[i], 1))

        heapify(session)

        for _ in range(k):
            minCost, group = heappop(session)
            res += minCost
            if p1+1< p2:
                if group == 0:
                    p1 += 1
                    heappush(session, (costs[p1], 0))
                elif group == 1:
                    p2 -= 1
                    heappush(session, (costs[p2], 1))
        
        return res