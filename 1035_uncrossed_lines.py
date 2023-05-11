class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:

        # T: O(n*m)
        # S: O(n*m)
    
        n, m = len(nums1), len(nums2)

        cache = {}
        def dfs(i,j):
            if (i,j) in cache:
                return cache[(i,j)]
            if i == n or j == m:
                return 0
            else:
                if nums1[i] == nums2[j]:
                    cache[(i,j)] = 1+dfs(i+1,j+1)
                else:
                    cache[(i,j)] = max(dfs(i,j+1), dfs(i+1,j))
                return cache[(i,j)]
        
        return dfs(0,0)
