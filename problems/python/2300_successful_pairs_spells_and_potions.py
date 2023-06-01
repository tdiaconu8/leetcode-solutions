from math import ceil

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:

        potions.sort()
        n = len(potions)
        res = []

        def searchMinPotion(target):
            l, r = 0, len(potions)-1
            while l < r:
                m = (l+r)//2
                if potions[m] < target:
                    l = m+1
                elif potions[m] >= target:
                    r = m
            return l

        for i in range(len(spells)):
            curSpell = spells[i]
            minPotion = ceil(success/curSpell)
            if minPotion > potions[-1]:
                res.append(0)
                continue
            res.append(n-searchMinPotion(minPotion))
        
        return res

        # T: O(n.log(m))
        # S: O(n)
