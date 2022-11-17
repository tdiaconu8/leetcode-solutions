class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        
        # Constants
        L1, l1 = (ax2 - ax1), (ay2 - ay1)
        L2, l2 = (bx2 - bx1), (by2 - by1)

        # Compute both areas
        a1 = L1 * l1
        a2 = L2 * l2
        print(a1, a2)

        # Compute area of intersection
        dx = min(ax2, bx2) - max(ax1, bx1)
        dy = min(ay2, by2) - max(ay1, by1)
        if ax2 < bx1 or ay1 > by2 or ax1 > bx2 or ay2 < by1:
            aoi = 0
        else:
            aoi = dx*dy

        return a1 + a2 - aoi