from heapq import heappush
import heapq
from typing import List


def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
    
    rows = []
    
    for i in range(len(mat)):
        heappush(rows, [sum(mat[i]), i])
    
    return [elem[1] for elem in heapq.nsmallest(k, rows)]

# Time : O(n)
# Space : O(n)