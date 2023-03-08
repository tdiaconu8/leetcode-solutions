from math import ceil

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        l, r = 1, max(piles)

        # Function that returns the nb of hours needed to eat all bananas piles with speed k per hr
        def nbHours(k):
            return sum(ceil(p/k) for p in piles)
        
        # BINARY SEARCH
        while l < r:
            m = (l+r)//2
            hours = nbHours(m)
            if hours > h:
                l = m+1
            else:
                r = m
        
        return l

        # n -> len(piles), m -> max(piles)
        # T: O(n*log(m))
        # S: O(1)
