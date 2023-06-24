class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:

        # T: O(n^3)
        # S: O(n^3)

        n = len(rods)
        totalHeight = sum(rods)
        res = 0

        cache = {}
        def helper(i, diff):
            if (i, diff) in cache:
                return cache.get((i, diff))
            if i == n:
                return 0 if diff == 0 else -float("inf")
            res = 0
            res = max(
                rods[i] + helper(i+1, diff + rods[i]),  # take the rod
                helper(i+1, diff - rods[i]),    # put the rod in the other set
                helper(i+1, diff))  # skip ip
            cache[(i,diff)] = res
            return res

        
        return helper(0,0)