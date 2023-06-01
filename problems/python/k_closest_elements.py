from heapq import *
from typing import List

# T: O(max(n, klogn))
# S: O(k)

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        minHeap = []
        heapify(minHeap)
        
        for val in arr:
            dist = abs(val-x)
            heappush(minHeap, (dist, val))
        
        res = []
        while k > 0:
            _, num = heappop(minHeap)
            res.append(num)
            k -= 1
            
        res.sort()
        return res