class Solution:
    def stoneGameII(self, piles: List[int]) -> int:

        n = len(piles)

        @cache
        def dfs(alice, i, M):
            if i >= n:
                return 0
            curStones = 0
            res = 0 if alice else float("inf")
            for X in range(1, 2*M+1):
                if i + X > n:
                    break
                curStones += piles[i + X - 1]
                if alice:
                    res = max(res, curStones + dfs(not alice, i+X, max(M, X)))
                elif not alice:
                    res = min(res, dfs(not alice, i+X, max(M, X)))
            return res

            
        
        return dfs(True, 0, 1)
