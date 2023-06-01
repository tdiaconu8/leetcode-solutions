class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:

        n = len(candies)
        mx = max(candies)
        res = []

        for i in range(n):
            if candies[i] + extraCandies >= mx:
                res.append(True)
            else:
                res.append(False)
        
        return res

        # T: O(n)
        # S: O(n)
