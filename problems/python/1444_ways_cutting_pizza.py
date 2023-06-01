class Solution:
    def ways(self, pizza: List[str], k: int) -> int:

        k -= 1
        n, m = len(pizza), len(pizza[0])
        MOD = 10**9+7

        def hasApple(r1, c1, r2, c2): # Check if there is an apple in the sub pizza
            for i in range(r1, r2):
                for j in range(c1, c2):
                    if pizza[i][j] == 'A':
                        return True
            return False
        
        
        @cache
        def dfs(r, c, cuts):

            if not hasApple(r, c, n, m):
                return 0

            if cuts == 0:
                return 1
            
            res = 0
            # CUT HORIZONTALLY
            for i in range(r+1, n):
                if hasApple(r, c, i, m):
                    res += dfs(i, c, cuts-1)

            # CUT VERTICALLY
            for j in range(c+1, m):
                if hasApple(r, c, n, j):
                    res += dfs(r, j, cuts-1)
            
            return res

        return dfs(0, 0, k) % MOD

        
