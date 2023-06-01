from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        m, n = len(board), len(board[0])
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(i, j, vis, curIndex):
            if (i<0 
                or i>=m 
                or j<0 
                or j>=n 
                or curIndex >= len(word) 
                or board[i][j] != word[curIndex] 
                or(i, j) in vis):
                    return False
            if curIndex == len(word)-1 and board[i][j] == word[curIndex]:
                return True
            else:
                vis.add((i, j))
                res = (dfs(i+1, j, vis, curIndex+1)
                        or dfs(i-1, j, vis, curIndex+1)
                        or dfs(i, j-1, vis, curIndex+1) 
                        or dfs(i, j+1, vis, curIndex+1))
                vis.remove((i, j))
                return res
                
        
        for i in range(m):
            for j in range(n):
                if dfs(i, j, set(), 0):
                    return True
        
        return False