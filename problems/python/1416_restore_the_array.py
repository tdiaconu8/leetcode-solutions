class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:

        n = len(s)
        MOD = 10**9+7

        cache = [None]*(n+1)
        def dfs(i):
            if cache[i]:
                return cache[i]
            if i == n:
                return 1
            if s[i] == "0":
                return 0
            res = 0
            for j in range(i+1, n+1):
                curNb = int(s[i:j])
                if curNb > k:
                    break
                res += dfs(j)
            cache[i] = res%MOD
            return res
        
        return dfs(0)%MOD
