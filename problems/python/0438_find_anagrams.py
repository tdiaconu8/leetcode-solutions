class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        n, m = len(s), len(p)
        # Edge case
        if m > n:
            return []
        
        res = []
        counterP = Counter(p)
        counterS = Counter(s[:m])
        for i in range(n-m+1):
            if counterS == counterP:
                res.append(i)
            counterS[s[i]] -= 1
            if i+m < n:
                counterS[s[i+m]] += 1
        return res

        '''
        T: O(n*m)
        S: O(n+m)
        '''
