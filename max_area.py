from typing import List


def maxArea(h: List[int]) -> int:
    
    res, n = 0, len(h)
    
    l, r = 0, n-1
    
    while l < r:
        area = min(h[l], h[r])*(r-l)
        res = max(res, area)
        if h[l] >= h[r]:
            r -= 1
        else:
            l += 1
            
    
    return res

'''
Time : O(n)
Space : O(1)
'''