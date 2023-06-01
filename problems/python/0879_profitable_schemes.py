class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:

        m = len(group)
        MOD = 10**9+7

        # ith crime, p remaining members, curProfit current profit -> # schemes that can be chosen
        cache = {}
        def dfs(i, p, curProfit):
            if (i,p,curProfit) in cache:
                return cache.get((i,p,curProfit))
            if i == m:
                if curProfit >= minProfit and p >= 0:
                    return 1
                return 0
            res = 0
            res += dfs(i+1, p, curProfit) # Skip the current crime
            # We take the current crime if it is possible
            if p-group[i] >= 0:
                newProfit, newPeople = curProfit + profit[i], p - group[i]
                res += dfs(i+1, newPeople, min(minProfit, newProfit))
            cache[(i,p,curProfit)] = res
            return res

        return dfs(0, n, 0)%MOD
      
      # T: 0(n*m*p)
      # S: O(n*m*p)
