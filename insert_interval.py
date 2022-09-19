from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], new: List[int]) -> List[List[int]]:
        
        res, n = [], len(intervals)
        for i in range(n):
            if new[1] < intervals[i][0]:
                res.append(new)
                return res + intervals[i:]
            elif new[0] > intervals[i][1]:
                res.append(intervals[i])
            else:
                new = [min(intervals[i][0], new[0]), max(intervals[i][1], new[1])]
        
        res.append(new)
        
        return res