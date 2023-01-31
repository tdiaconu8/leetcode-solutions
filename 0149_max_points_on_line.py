from collections import defaultdict

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:

        n, res = len(points), 1

        def getSlop(p1, p2):   # function that returns the slop of the line between two points
            x1, y1 = p1
            x2, y2 = p2
            if x1 == x2:
                return float('inf')
            return (y2-y1)/(x2-x1)

        for i in range(n-1):
            p1 = points[i]
            counter = defaultdict(int)
            for j in range(i+1, n):
                p2 = points[j]
                slop = getSlop(p1, p2)
                counter[slop] += 1
                res = max(res, counter[slop]+1)
        
        return res
        
        '''
        T: O(n^2)
        S: O(n)
        '''
