class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:

        cache = {}

        def dfs(a, b):
            if a == b:
                return True
            if (a, b) in cache:
                return cache[(a,b)]
            else:
                n = len(a)
                for i in range(1, n):
                    if dfs(a[:i], b[-i:]) and dfs(a[i:], b[:n-i]):
                        cache[(a, b)] = True
                        return True
                    if dfs(a[:i], b[:i]) and dfs(a[i:], b[i:]):
                        cache[(a, b)] = True
                        return True
                cache[(a, b)] = False
                return False
        
        return dfs(s1, s2)

        # T: O(n^4)
        # S: O(n^3)
