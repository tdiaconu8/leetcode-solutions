class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:

        n = len(board)
        lookup = [None] * (n*n+1)
        reverse, square = True, 1
        for i in range(n-1, -1, -1):
            if reverse:
                for j in range(n):
                    lookup[square] = (i, j)
                    square += 1
            elif not reverse:
                for j in range(n-1, -1, -1):
                    lookup[square] = (i, j)
                    square += 1
            reverse = not reverse

        queue = deque([])
        queue.append((1, 0))
        vis = set()
        res = float('inf')

        while queue:
            square, dist = queue.popleft()
            for i in range(1, 7):
                nextSquare = square+i
                row, col = lookup[nextSquare]
                if board[row][col] != -1:
                    nextSquare = board[row][col]
                if nextSquare == n*n:
                    return dist+1
                if nextSquare not in vis:
                    vis.add(nextSquare)
                    queue.append((nextSquare, dist+1))
    
        return -1
