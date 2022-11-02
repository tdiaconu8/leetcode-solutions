from collections import deque
from typing import List

class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:

        # Function to compute the number of differences between two equal length strings
        def differ(g1, g2):
            diff = 0
            for i in range(len(g1)):
                if g1[i] != g2[i]:
                    diff += 1
            return diff

        queue = deque([(start, 0)])
        res = float('inf')
        seen = set()

        while queue:
            seq, mut = queue.popleft()
            if differ(seq, end) == 0:
                res = min(res, mut)
            for gene in bank:
                if gene not in seen and differ(seq, gene) == 1:
                    queue.append((gene, mut +1))
                    seen.add(gene)

        return res if res != float('inf') else -1