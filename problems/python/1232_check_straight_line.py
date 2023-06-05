class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:

        # T: O(n)
        # S: O(1)

        n = len(coordinates)

        x1, y1 = coordinates[0][0], coordinates[0][1]
        x2, y2 = coordinates[1][0], coordinates[1][1]

        slope = float("inf") if x1 == x2 else (y2-y1)/(x2-x1)

        for i in range(2, n):
            x, y = coordinates[i][0], coordinates[i][1]
            curSlope = float("inf") if x == x1 else (y-y1)/(x-x1)
            if curSlope != slope:
                return False
            
        return True