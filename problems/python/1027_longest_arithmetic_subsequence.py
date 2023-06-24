from collections import defaultdict

class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:

        res = 0
        n = len(nums)

        dp = [ defaultdict(int) for _ in range(n)]

        for i in range(n):
            dp[i][501] = 1
            for j in range(i):
                diff = nums[i] - nums[j]
                if dp[j][diff]:
                    dp[i][diff] = 1 + dp[j][diff]
                else:
                    dp[i][diff] = 2
            res = max(res, max(dp[i].values()))
        
        return res
        
        
        
        # MEMOIZATION: TLE
        '''
        # i index in nums array, diff is the current arithmetic reason
        cache = {}
        def dfs(i, diff):
            if i >= n:
                return 0
            if (i, diff) in cache:
                return cache.get((i, diff))
            res = 1
            if diff > 500:
                for j in range(i+1, n):
                    res = max(res, 1 + dfs(j, nums[j]-nums[i]), dfs(j, 5000))
            else:
                for j in range(i+1, n):
                    if nums[j]-nums[i] == diff:
                        res = max(res, 1 + dfs(j, diff))
            cache[(i, diff)] = res
            return res
        
        return dfs(0, 5000)
        '''