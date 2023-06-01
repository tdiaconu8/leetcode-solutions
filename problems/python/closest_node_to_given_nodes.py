class Solution:
    def closestMeetingNode(self, edges: List[int], n1: int, n2: int) -> int:

        # compute the distances from node 1 to all nodes
        # compte the distances from node 2 to all nodes
        # return the min-max of the two arrays

        n = len(edges)
        dists = [[-1, -1] for _ in range(n)]

        def dfs(node, vis, dist, idx):
            if node == -1 or node in vis:
                return
            dists[node][idx] = dist
            vis.add(node)
            dfs(edges[node], vis, dist+1, idx)
            vis.remove(node)
            return
        
        # Two dfs
        dfs(n1, set(), 0, 0)
        dfs(n2, set(), 0, 1)
        
        res, minDist = -1, float('inf')
        for i in range(n):
            a, b = dists[i]
            if a == -1 or b == -1:
                continue
            curMax = max(a, b)
            if curMax < minDist:
                res = i
                minDist = curMax

        return res
