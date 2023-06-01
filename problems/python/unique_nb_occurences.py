from typing import List

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:

        counter = {}

        for val in arr:
            counter[val] = counter.get(val, 0) + 1
        
        occ = set()

        for _, c in counter.items():
            if c in occ:
                return False
            occ.add(c)
        
        return True

'''
T: O(n)
S: O(n)
'''