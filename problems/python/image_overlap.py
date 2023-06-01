from typing import List

class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:

        n = len(img1)
        def helper(di, dj):
            overlap = 0
            for i in range(n):
                for j in range(n):
                    if 0<=i+di<n and 0<=j+dj<n and img1[i+di][j+dj] == 1 and img1[i+di][j+dj] == img2[i][j]:
                        overlap += 1
            return overlap
        
        return max([helper(r, c) for r in range(-n,n) for c in range(-n,n)])