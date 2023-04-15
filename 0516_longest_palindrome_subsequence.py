class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:

        n = len(s)

        cache = {}
        def dfs(start, end):
            if (start, end) in cache:
                return cache[(start, end)]
            if start > end:
                return 0
            if start == end:
                return 1
            if s[start] == s[end]:
                res = 2 + dfs(start+1, end-1)
                cache[(start, end)] = res
                return res
            if s[start] != s[end]:
                res = max(dfs(start+1, end), dfs(start, end-1))
                cache[(start, end)] = res
                return res
        
        return dfs(0, n-1)
