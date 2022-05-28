from typing import List


def findAnagrams(s: str, p: str) -> List[int]:
    
    n,m = len(s), len(p)
    
    if m > n:
        return []
    
    else:
        indexes, sChars, pChars = [], {}, {}
        for i in range(m):
            pChars[p[i]] = 1 + pChars.get(p[i], 0)
            sChars[s[i]] = 1 + sChars.get(s[i], 0)
        if sChars == pChars:
            indexes.append(0)
        l = 0
        for i in range(m,n):
            sChars[s[i]] = 1 + sChars.get(s[i], 0)
            sChars[s[l]] -= 1
            if sChars[s[l]] == 0:
                sChars.pop(s[l])
            l += 1
            if sChars == pChars:
                indexes.append(l)
        return indexes

s = "abab"
p = "ab"

print(findAnagrams(s,p))