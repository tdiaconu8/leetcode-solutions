class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:

        # T: O(n²)
        # S: O(n²)
        res = 0

        n = len(grid)
        rows = defaultdict(int)

        for i in range(n):
            sequence = ""
            for j in range(n):
                sequence += str(grid[i][j]) + "/"
            rows[sequence] += 1
        
        for j in range(n):
            sequence = ""
            for i in range(n):
                sequence += str(grid[i][j]) + "/"
            res += rows[sequence]
        
        return res