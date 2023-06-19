class Solution:
    def largestAltitude(self, gain: List[int]) -> int:

        # T: O(n)
        # S: O(1)     

        cur, res = 0, 0

        for diff in gain:
            cur += diff
            res = max(res, cur)
        
        return res