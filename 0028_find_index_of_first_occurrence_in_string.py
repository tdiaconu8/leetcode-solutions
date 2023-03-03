class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        n, m = len(haystack), len(needle)

        if m > n: # EDGE CASE
            return -1
        
        i, j = 0, 0

        for i in range(n-m+1):
            while (i+j) < n and j < m and haystack[i+j] == needle[j]:
                j += 1
            if j == m:
                return i
            i += 1
            j = 0
        
        return -1

        # T: O(n^2)
        # S: O(1) -> no extra space used
