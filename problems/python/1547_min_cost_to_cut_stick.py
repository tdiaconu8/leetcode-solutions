from collections import defaultdict

class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:

        # MEMOIZATION
        # T: O(n²)
        # S: O(n²)

        cache = defaultdict(int)
        def dfs(l, r):
            if r - l <= 1:
                return 0
            if (l, r) in cache:
                return cache[(l, r)]
            res = float("inf")
            for cut in cuts:
                # We chose only cuts that are possible
                if l < cut < r:
                    res = min(
                        res,
                        r - l + dfs(l, cut) + dfs(cut, r)
                    )
            res = res if res != float("inf") else 0
            cache[(l, r)] = res
            return res

        return dfs(0, n)
