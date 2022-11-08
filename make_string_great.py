class Solution:
    def makeGood(self, s: str) -> str:

        n = len(s)
        print(s, n)
        for i in range(n-1):
            if (s[i].isupper() and s[i].lower() == s[i+1]) or (s[i+1].isupper() and s[i] == s[i+1].lower()):
                s = self.makeGood(s[:i] + s[i+2:])
                break
        
        return s