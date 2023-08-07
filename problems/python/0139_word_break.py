class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        # T: O(2^n)
        # S: O(2^n)

        n = len(s)

        cache = {}
        def dfs(curr):
            if curr in cache:
                return cache[curr]
            cache[curr] = False
            if len(curr) > n or curr != s[:len(curr)]:
                return False
            if curr == s:
                cache[curr] = True
                return True
            for word in wordDict:
                if dfs(curr + word):
                    cache[curr] = True
                    return True
            return False
        
        return dfs("")