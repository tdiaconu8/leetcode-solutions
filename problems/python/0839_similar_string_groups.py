from collections import defaultdict

class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:

        # Utils function to determine if two strings are equivalent or not
        def isEquivalent(s1, s2):
            n = len(s1)
            diff = 0
            for i in range(n):
                if s1[i] != s2[i]:
                    diff += 1
            return diff == 0 or diff == 2

        # Build graph: node are connected if their strings are equivalent
        n = len(strs)
        graph = defaultdict(list)
        for i in range(n-1):
            for j in range(i+1, n):
                if isEquivalent(strs[i], strs[j]):
                    graph[i].append(j)
                    graph[j].append(i)
        
        vis = set()

        def dfs(i):
            if i in vis:
                return
            vis.add(i)
            for neigh in graph[i]:
                dfs(neigh)

        res = 0
        for i in range(n):
            if i not in vis:
                res += 1
                dfs(i)
        
        return res

        # T: O(n^2*m^2)
        # S: O(n^2)
