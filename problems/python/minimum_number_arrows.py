from typing import List

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:

        points.sort()
        s, e = points[0]
        res = 1

        for i in range(1, len(points)):
            x1, x2 = points[i]
            if s <= x1 <= e:
                e = min(x2, e)
            else:
                res += 1
                s, e = x1, x2
        
        return res

        '''
        T: O(nlogn)
        S: O(1)
        '''