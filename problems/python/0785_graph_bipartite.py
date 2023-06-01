from collections import deque

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:

        # T: O(E+V), S: O(E+V)

        n = len(graph)
        sets = [0]*n    # map the node i to its set: 1 for A, -1 for B

        for i in range(n):
            if sets[i]:     # if the node already belongs to set, we skip
                continue
            # else, we loop over all neighbors and split the nodes in the two independent sets
            q = deque([(i, 1)])
            while q:
                node, s = q.popleft()
                if not sets[node]:
                    sets[node] = s
                    for neigh in graph[node]:
                        q.append((neigh, -s))
                elif sets[node] != s:   # if the node already belongs to a set that is in conflict with the curr, we return False
                    return False

        return True
