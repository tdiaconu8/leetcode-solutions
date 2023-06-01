from collections import defaultdict, deque

class Solution:
    def minJumps(self, arr: List[int]) -> int:

        n = len(arr)
        values = defaultdict(list)

        for i, val in enumerate(arr):
            values[val].append(i)

        queue = deque([(0, 0)])
        vis = {0}

        while queue:
            curPos, jumps = queue.popleft()
            if curPos == n-1:
                return jumps
            for nextPos in values[arr[curPos]]:
                if nextPos not in vis:
                    queue.append((nextPos, jumps +1))
                    vis.add(nextPos)
            values[arr[curPos]] = []
            for neigh in [curPos-1, curPos+1]:
                if 0 <= neigh < n and neigh not in vis:
                    queue.append((neigh, jumps +1))
                    vis.add(neigh)

        return -1

        # T: O(n)
        # S: O(n)
