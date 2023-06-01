from typing import List


def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    
    ans = []
    intervals.sort()
    cur = [intervals[0][0], intervals[0][1]]
    
    for i in range(1, len(intervals)):
        s, e = intervals[i][0], intervals[i][1]
        if s > cur[1]:
            ans.append(cur)
            cur = [s,e]
        else:
            cur[1] = max(cur[1], e)
    
    ans.append(cur)
    return ans

'''
T: O(nlogn)
S: O(n)
'''