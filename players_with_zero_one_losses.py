from typing import List

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:

        wins, defeats = {}, {}

        for m in matches:
            w, l = m
            wins[w] = wins.get(w, 0) + 1
            defeats[l] = defeats.get(l, 0) + 1
        
        res = [[], []]

        for p in wins:
            if p not in defeats:
                res[0].append(p)
        
        for p in defeats:
            if defeats[p] == 1:
                res[1].append(p)
        
        res[0].sort()
        res[1].sort()
        return res