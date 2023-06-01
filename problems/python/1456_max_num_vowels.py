class Solution:
    def maxVowels(self, s: str, k: int) -> int:

        n = len(s)
        vowels = set(['a', 'e', 'i', 'o', 'u'])

        l, r = 0, k-1
        res, cur = 0, 0
        for i in range(k):
            if s[i] in vowels:
                cur += 1
        
        res = cur
        
        while r < n-1:
            if s[l] in vowels:
                cur -= 1
            if s[r+1] in vowels:
                cur += 1
            res = max(res, cur)
            l += 1
            r += 1
        
        return res

        # T: O(n)
        # S: O(1)
