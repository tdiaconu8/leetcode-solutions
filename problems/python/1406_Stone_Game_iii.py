from collections import defaultdict

class Solution:
    def stoneGameIII(self, stones: List[int]) -> str:
        
        # MEMOIZATION
        # T: O(n)
        # S: O(n)
        
        n = len(stones)

        cache = defaultdict(int)
        def dfs(i):
            if i == n:
                return 0
            if cache[i]:
                return cache[i]
            res = stones[i] - dfs(i+1)
            if i + 1 < n:
                res = max(res, stones[i] + stones[i+1] - dfs(i+2))
            if i + 2 < n:
                res = max(res, stones[i] + stones[i+1] + stones[i+2] - dfs(i+3))
            cache[i] = res
            return res
            
        
        res = dfs(0)

        if res > 0:
            return "Alice"
        elif res < 0:
            return "Bob"
        return "Tie"
        

