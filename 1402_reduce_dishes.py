class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:

        n = len(satisfaction)
        cache = {}

        def dfs(i, t):
            if i == n:
                return 0
            if (i, t) in cache:
                return cache[(i,t)]
            else:
                res = max((t*satisfaction[i]+dfs(i+1, t+1)), dfs(i+1, t))
                cache[(i,t)] = res
                return res
        
        satisfaction.sort() # sort the satisfaction array to keep the largest satisfactions for higher times values
        return dfs(0, 1)

        # T: O(n*n)
        # S: O(n*n) -> cache
