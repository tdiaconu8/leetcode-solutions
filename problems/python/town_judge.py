class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:

        # edge case
        if not trust:
            return 1 if n == 1 else -1
    
        trusters = defaultdict(set)
        graph = defaultdict(list)

        for a, b in trust:
            trusters[b].add(a)
            graph[a].append(b)
        
        for key, val in trusters.items():
            if len(val) == n-1 and not graph[key]:
                return key

        return -1
