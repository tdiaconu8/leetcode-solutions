from collections import defaultdict

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:

        n = len(manager)
        graph = defaultdict(list)

        for i in range(n):
            manag = manager[i]
            if manag != -1:
                graph[manag].append(i)
        
        def dfs(id, time):
            res = time
            for neigh in graph[id]:
                res = max(res, dfs(neigh, time + informTime[id]))
            return res

        return dfs(headID, 0)