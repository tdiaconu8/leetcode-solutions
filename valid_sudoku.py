from collections import defaultdict
from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        lines, cols, subSquares = defaultdict(set), defaultdict(set), defaultdict(set)

        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val == '.':
                    continue
                if val in lines[i]:
                    return False
                lines[i].add(val)
                if val in cols[j]:
                    return False
                cols[j].add(val)
                squareX, squareY = i//3, j//3
                if val in subSquares[(squareX, squareY)]:
                    return False
                subSquares[(squareX, squareY)].add(val)

        return True