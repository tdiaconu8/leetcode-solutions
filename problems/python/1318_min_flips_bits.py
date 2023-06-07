class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:

        # T: O(log2(10**9)) ~ 30
        # S: O(1)

        # ALGO: we will check bits one by one
        # BIT MANIPULATION
        res = 0

        while a or b or c:
            if (c & 1) and (a & 1) | (b & 1) != c & 1:
                res += 1
            if not (c & 1) and (a & 1) | (b & 1) != 0:
                res += 2 if (a & 1 == 1 and b & 1 == 1) else 1
            a, b, c = a >> 1, b >> 1, c >> 1
        
        return res