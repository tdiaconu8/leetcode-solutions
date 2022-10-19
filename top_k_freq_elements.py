from typing import List
from heapq import *

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        h = []
        heapify(h)
        counter = {}

        for w in words:
            counter[w] = counter.get(w, 0) + 1
        
        for key, val in counter.items():
            heappush(h, (-val, key))
        
        res = []
        while k > 0:
            _, word = heappop(h)
            res.append(word)
            k -= 1
        
        return res

'''
T: O(n)
S: O(n)
'''