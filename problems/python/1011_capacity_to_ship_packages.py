class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        n = len(weights)
        l, r = max(weights), sum(weights)

        def canShip(cap):
            res, curCap = 0, 0
            for i, w in enumerate(weights):
                if w > cap:
                    return False
                if curCap + w > cap:
                    curCap = 0
                    res += 1
                curCap += w
            return res+1 <= days
        
        while l < r:
            m = (l+r)//2
            if canShip(m):
                r = m
            else:
                l = m+1
        
        return l
    
    # n -> len(weights), m -> sum(weights)
    # T: O(n*logm)
    # S: O(1)
