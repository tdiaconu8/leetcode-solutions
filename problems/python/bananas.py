from typing import List
import math
from math import *

### Brute Force
def minEatingSpeedBF(piles: List[int], h: int) -> int:
        if len(piles) == 1:
            return math.ceil(piles[0]/h)
        else:
            k = 1
            hr = h+1
            while hr != h:
                hr = 0
                for p in piles:
                    hr += math.ceil(p/k)
                if hr == h:
                    return k, hr
                else:
                    k += 1

### Binary Search
def minEatingSpeed(piles: List[int], h: int) -> int:
        if len(piles) == 1:
            return math.ceil(piles[0]/h)
        else:
            l, r = 1, max(piles)
            while l < r:
                k = (l + r)//2
                hr = 0
                for p in piles:
                    hr += math.ceil(p/k)
                if hr > h:
                    l = k+1
                else:
                    return k

piles = [30,11,23,4,20]
h = 6

print(minEatingSpeed(piles, h))