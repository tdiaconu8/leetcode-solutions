class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        n, m, p = len(s1), len(s2), len(s3)

        if n + m != p:
            return False
        
        @cache
        def helper(i, j):
            if i == n and j == m:
                return True
            if i == n:
                if s2[j] == s3[i+j] and helper(i, j+1):
                    return True
            elif j == m:
                if s1[i] == s3[i+j] and helper(i+1, j):
                    return True
            else:
                if s1[i] == s3[i+j]:
                    if helper(i+1, j):
                        return True
                if s2[j] == s3[i+j]:
                    if helper(i, j+1):
                        return True
            return False
        
        return helper(0, 0)