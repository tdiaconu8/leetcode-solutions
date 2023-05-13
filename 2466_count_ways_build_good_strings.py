class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:

        # MEMOIZATION
        # T: O(high)
        # S: O(high)

        MOD = 10**9+7

        cache = {}
        def dfs(i):
            if i > high:
                return 0
            if i in cache:
                return cache.get(i)
            tmp = 0
            if low <=i <= high:
                tmp += 1
            tmp += dfs(i+zero) + dfs(i+one)
            cache[i] = tmp
            return tmp % MOD
        
        return dfs(0)
