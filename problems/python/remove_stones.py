from typing import List

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:

        class UnionFind:
            def __init__(self, n):
                self.par = [i for i in range(n)]
                self.rank = [1 for i in range(n)]
                self.count = n
            
            def find(self, x):
                if self.par[x] != x:
                    self.par[x] = self.find(self.par[x])
                return self.par[x]
            
            def union(self, x, y):
                p1, p2 = self.find(x), self.find(y)
                if p1 != p2:
                    if self.rank[p1] > self.rank[p2]:
                        self.par[p2] = p1
                    else:
                        self.par[p1] = self.par[p2]
                        if p1 == p2:
                            self.rank[p1] += 1
                    self.count -= 1

        N = len(stones)
        uf = UnionFind(N)
        
        for i in range(N-1):
            for j in range(i+1, N):
                if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                    uf.union(i,j)
        
        return N-uf.count