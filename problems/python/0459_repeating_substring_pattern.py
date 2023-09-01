class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:

        n = len(s)

        for i in range(1, n//2+1):
            pattern = s[:i]
            k = n//i
            if i*k == n and pattern*k == s:
                return True

        return False 
