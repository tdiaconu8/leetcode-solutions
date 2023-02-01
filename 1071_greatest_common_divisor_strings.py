class Solution:
    def gcdOfStrings(self, s1: str, s2: str) -> str:

        n, m = len(s1), len(s2)
        res = ''

        def isGcd(l):
            return s1[:l] == s2[:l] and (s1[:l]*(n//l) == s1 and s1[:l]*(m//l) == s2)

        for i in range(min(n, m), 0, -1):
            if isGcd(i):
                return s1[:i]
            
        
        return ''

        '''
        T: O(min(n,m)*(n+m))
        S: O(min(n,m))
        '''
