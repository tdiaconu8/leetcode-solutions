from heapq import *

class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:

        maxHeap = []
        mn = float('inf')

        for num in nums:
            if num % 2 != 0:
                heappush(maxHeap, -2*num)
                mn = min(mn, 2*num)
            else:
                heappush(maxHeap, -num)
                mn = min(mn, num)
        
        mx = -heappop(maxHeap)
        res = mx-mn
        
        while mx % 2 == 0:
            mn = min(mn, mx//2)
            heappush(maxHeap, -(mx//2))
            mx = -heappop(maxHeap)
            res = min(res, mx-mn)
        
        return res

        # T: O(nlogn)
        # S: O(n)
