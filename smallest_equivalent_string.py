class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:

        n, m = len(s1), len(baseStr)
        res = ''
        graph = defaultdict(list)
        par = {}
        
        # Union find
        def union(x, y):
            parX, parY = find(x), find(y)
            if parX != parY:
                if parX < parY:
                    par[parY] = parX
                else:
                    par[parX] = parY
        def find(x):
            if x != par[x]:
                par[x] = find(par[x])
            return par[x]
        
        for i in range(n):
            par[s1[i]] = s1[i]
            par[s2[i]] = s2[i]
        for i in range(m):
            par[baseStr[i]] = baseStr[i]
        
        for i in range(n):
            a, b = s1[i], s2[i]
            union(a, b)
        
        for char in baseStr:
            res += find(char)
        
        return res
