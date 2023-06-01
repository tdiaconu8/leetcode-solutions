# An integer array original is transformed into a doubled array changed by appending twice the value of every element in original, and then randomly shuffling the resulting array.

# Given an array changed, return original if changed is a doubled array. If changed is not a doubled array, return an empty array. The elements in original may be returned in any order.


from collections import Counter
from typing import List


class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        
        n = len(changed)
        if (n%2 != 0):
            return None
        
        changed.sort()
        
        counter = {}
        for num in changed:
            counter[num] = counter.get(num, 0) + 1
        counter = Counter(changed)
        
        res = []
        for i, val in enumerate(changed):
            if counter[val] == 0:
                continue
            elif 2*val not in counter or counter[2*val] == 0:
                return None
            elif val == 0 and counter[val] < 2:
                return None
            else:
                res.append(val)
                counter[val] -= 1
                counter[2*val] -= 1
        
        return res