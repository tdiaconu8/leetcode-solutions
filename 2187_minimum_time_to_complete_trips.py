class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:

        l, r = 0, max(time)*totalTrips

        def computeTrips(T):
            return sum(T//t for t in time)

        while l < r:
            m = (l+r)//2
            trips = computeTrips(m)
            if trips < totalTrips:
                l = m+1
            else:
                r = m
        
        return l

        # T: O(n*log(t))
        # S: O(1)
