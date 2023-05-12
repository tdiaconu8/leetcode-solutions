from collections import defaultdict

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:

        # T: O(n), S: O(n)

        # DP approach
        # Zero-one Knapsack
        n = len(questions)
        dp = defaultdict(int)

        for i in range(n-1, -1, -1):
            pts, skip = questions[i]
            dp[i] = max(
                pts + dp[i+skip+1], # SOLVE
                dp[i+1]# SKIP
            )
        return dp[0]
                
        

        
        # Recursion -> MEMOIZATION
        '''
        n = len(questions)
        cache = [0]*n
        def dfs(i):
            if i >= n:
                return 0
            if cache[i]:
                return cache[i]
            pts, skip = questions[i]
            tmp = max(pts+dfs(i+skip+1), dfs(i+1))
            cache[i] = tmp
            return tmp
        
        return dfs(0)
        '''
