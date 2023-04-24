from heapq import *

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        stones = [-x for x in stones]
        heapify(stones)

        while len(stones) > 1:
            x, y = heappop(stones), heappop(stones)
            if x < y:
                heappush(stones, x-y)
            if x > y:
                heappush(stones, y-x)
        
        return -stones[0] if stones else 0

        # T: O(log(n!))
        # S: O(n)
