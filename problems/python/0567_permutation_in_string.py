class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        n, m = len(s1), len(s2)
        if n > m: # Edge case
            return False
        
        counter = Counter(s1)

        # helper function -> return True if one s1 permutation is string s
        def isPermutation(s1, s): 
            tmp = Counter(s)
            if len(tmp) != len(counter):
                return False
            for key, val in tmp.items():
                if key not in counter or val != counter[key]:
                    return False
            return True

        for i in range(m-n+1):
            subString = s2[i:i+n]
            if isPermutation(s1, subString):
                return True
        return False

        '''
        T: O(n+m*n)
        S: O(n+m)
        '''
