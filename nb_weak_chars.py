from typing import List


class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        
        n = len(properties)
        res = 0
        
        properties.sort(key = lambda x: (-x[0], x[1]))
        maxDef = 0
        for _, defense in properties:
            if defense < maxDef:
                res += 1
            else:
                maxDef = defense
        
        return res